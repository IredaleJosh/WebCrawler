import unittest
from unittest.mock import patch, Mock
from src.indexer import tokenise, build_indexer

class CrawlerTest(unittest.TestCase):
    # Test Tokeniser for Case Sensitivity, Punctuation and Accented Characters
    def test_tokenise_characters(self):
        text = "HéLLo hElLo.... HELLO?????"
        test = tokenise(text)
        result = ["héllo", "hello", "hello"]
        self.assertEqual(test, result)

    # Test Tokeniser for Empty Space
    def test_tokenise_empty(self):
        text = ""
        test = tokenise(text)
        result = []
        self.assertEqual(test, result)

    # Test Tokeniser for Non-string
    def test_tokenise_not_string(self):
        textBool = True
        textInteger = 20
        testBool = tokenise(textBool)
        testInteger = tokenise(textInteger)
        result = []
        self.assertEqual(testBool, result)
        self.assertEqual(testInteger, result)

    # TEST INDEXING OF SINGLE PAGE WITH SIMPLE TEXT
    def test_simple_page(self):
        pages = [
            {"page":"pageOne",
             "text":"Simple Quote",}
        ]
        indexer = build_indexer(pages)
        self.assertIn("simple", indexer)
        self.assertIn("quote", indexer)
        self.assertIn("pageOne", indexer["simple"])
        self.assertIn("pageOne", indexer["quote"])

        self.assertEqual(indexer["simple"]["pageOne"]["frequency"], 1)
        self.assertEqual(indexer["quote"]["pageOne"]["frequency"], 1)

        self.assertEqual(indexer["simple"]["pageOne"]["positions"], [0])
        self.assertEqual(indexer["quote"]["pageOne"]["positions"], [1])

    # TEST MULTIPLE WORDS ACROSS PAGES
    def test_multiple_words_across_pages(self):
        pages = [
            {"page":"pageOne",
             "text":"Hello Hello World Hello World",},
            {"page":"pageTwo",
            "text":"Hello Again Hello Again",}
        ]
        indexer = build_indexer(pages)
        self.assertIn("hello", indexer)
        self.assertIn("pageOne", indexer["hello"])
        self.assertIn("pageTwo", indexer["hello"])

        self.assertEqual(indexer["hello"]["pageOne"]["frequency"], 3)
        self.assertEqual(indexer["hello"]["pageTwo"]["frequency"], 2)

        self.assertEqual(indexer["hello"]["pageOne"]["positions"], [0, 1, 3])
        self.assertEqual(indexer["hello"]["pageTwo"]["positions"], [0, 2])

    # TEST EMPTY WORDS MIXED INTO PAGES
    def test_multiple_words_across_pages(self):
        pages = [
            {"page":"pageOne",
             "text":"",},
            {"page":"pageTwo",
            "text":"Hello",}
        ]
        indexer = build_indexer(pages)
        self.assertIn("hello", indexer)
        for word in indexer:
            self.assertNotIn("pageOne", indexer[word])

if __name__ == "__main__":
    unittest.main()