import unittest
from unittest.mock import patch, Mock
from src.crawler import crawl_site

class CrawlerTest(unittest.TestCase):

    # TEST IT EXTRACTS AND STORES THE QUOTE AND PAGE
    @patch("src.crawler.requests.get")
    @patch("time.sleep", return_value=None)
    def test_crawl_page_extracts_text(self, mock_sleep, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = """
        <div class="quote">
            <span class="text">Hello World</span>
            <small class="author">Author</small>
        </div>
        """
        mock_get.return_value = mock_response

        result = crawl_site("https://quotes.toscrape.com")
        self.assertIn("hello world - author", result[0]["text"].lower())
        self.assertEqual(result[0]["page"], "https://quotes.toscrape.com")
    
    # TEST IT WHEN PAGE HAS NO QUOTES
    @patch("src.crawler.requests.get")
    @patch("time.sleep", return_value=None)
    def test_empty_quotes(self, mock_sleep, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = """
        <html><html>
        """
        mock_get.return_value = mock_response
        pages = crawl_site("https://quotes.toscrape.com")

        self.assertEqual(pages[0]["text"], "")

    # # TEST NEXT PAGE IS ACQUIRED
    # @patch("src.crawler.requests.get")
    # @patch("time.sleep", return_value=None)
    # def test_next_page(self, mock_sleep, mock_get):
    #     mock_response = Mock()
    #     mock_response.status_code = 200
    #     mock_response.text = """
    #     <li class="next"><a href="/page/2/">Next</a></li>
    #     """
    #     mock_get.return_value = mock_response
    #     pages = crawl_site("https://quotes.toscrape.com")

    #     self.assertEqual(pages[0]["next page"], "https://quotes.toscrape.com/page/2")

    # TEST STOPS WHEN NO MORE PAGES

    # TEST HANDLING OF HTTP ERRORS

    # TEST BROKEN HTML

if __name__ == "__main__":
    unittest.main()

