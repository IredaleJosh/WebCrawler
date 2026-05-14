import unittest
from unittest.mock import patch, Mock
from src.search import print_word, find_phrase

class SearchTest(unittest.TestCase):
    # WORD DOESN'T EXIST
    def test_print_no_result(self):        
        index = {
            "test": {"url_one": {"frequency": 1, "positions": [0]}}
        }
        result = print_word(index, "hello")
        self.assertEqual(result, {})

    # WORDS ACROSS PAGES + CASE SENSITIVITY
    def test_print_across_pages(self):        
        index = {
            "test": {
                "url_one": {"frequency": 1, "positions": [0]},
                "url_two": {"frequency": 1, "positions": [0]},
            }
        }
        result = print_word(index, "TEST")
        self.assertCountEqual(result,["url_one", "url_two"])

    # TEST FOR INCORRECT DATA
    def test_wrong_data(self):
        index = {
            "test": {"url_one": {"frequency": 1, "positions": [0]}}
        }
        result = print_word(index, True)
        result = print_word(index, 200)
        self.assertEqual(result, {})

    # MULTIPLE TYPES OF PHRASE RETURN CORRECT PAGES
    def test_search_phrase(self):        
        index = {
            "test": {
                "url_one": {"frequency": 1, "positions": [0]},
                "url_two": {"frequency": 1, "positions": [0]},
            },
            "data": {
                "url_one": {"frequency": 1, "positions": [1]},
            }
        }
        # PHRASE, SINGLE WORD, NO WORDS, CASE SENSITIVITY + WRONG DATA
        result_one = find_phrase(index, ['test', 'data'])
        result_two = find_phrase(index, ['test'])
        result_three = find_phrase(index, ['hello'])
        result_four = find_phrase(index, ['TEST'])
        result_five = find_phrase(index, 20)
        result_six = find_phrase(index, True)

        self.assertEqual(result_one,["url_one"])
        self.assertCountEqual(result_two,["url_one", "url_two"])
        self.assertEqual(result_three,[])
        self.assertCountEqual(result_four,["url_one", "url_two"])
        self.assertEqual(result_five,[])
        self.assertEqual(result_six,[])

if __name__ == "__main__":
    unittest.main()