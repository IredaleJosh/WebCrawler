import unittest
from unittest.mock import patch, Mock
from src.indexer import tokenise, build_indexer

class IndexerTest(unittest.TestCase):
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
            {"page":"url_one",
             "text":"Simple Quote",}
        ]
        indexer = build_indexer(pages)
        self.assertIn("simple", indexer)
        self.assertIn("quote", indexer)
        self.assertIn("url_one", indexer["simple"])
        self.assertIn("url_one", indexer["quote"])

        self.assertEqual(indexer["simple"]["url_one"]["frequency"], 1)
        self.assertEqual(indexer["quote"]["url_one"]["frequency"], 1)

        self.assertEqual(indexer["simple"]["url_one"]["positions"], [0])
        self.assertEqual(indexer["quote"]["url_one"]["positions"], [1])

    # TEST MULTIPLE WORDS ACROSS PAGES
    def test_multiple_words_across_pages(self):
        pages = [
            {"page":"url_one",
             "text":"Hello Hello World Hello World",},
            {"page":"url_two",
            "text":"Hello Again Hello Again",}
        ]
        indexer = build_indexer(pages)
        self.assertIn("hello", indexer)
        self.assertIn("url_one", indexer["hello"])
        self.assertIn("url_two", indexer["hello"])

        self.assertEqual(indexer["hello"]["url_one"]["frequency"], 3)
        self.assertEqual(indexer["hello"]["url_two"]["frequency"], 2)

        self.assertEqual(indexer["hello"]["url_one"]["positions"], [0, 1, 3])
        self.assertEqual(indexer["hello"]["url_two"]["positions"], [0, 2])

    # TEST EMPTY WORDS MIXED INTO PAGES
    def test_multiple_words_across_pages(self):
        pages = [
            {"page":"url_one",
             "text":"",},
            {"page":"url_two",
            "text":"Hello",}
        ]
        indexer = build_indexer(pages)
        self.assertIn("hello", indexer)
        for word in indexer:
            self.assertNotIn("url_one", indexer[word])

if __name__ == "__main__":
    unittest.main()