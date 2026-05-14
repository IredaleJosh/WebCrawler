## How the Crawler Works

Program crawls through the pages of the website: "https://quotes.toscrape.com" and collects quotes and creating an inverted index of all quotes, allowing user to find pages containing certain search terms.


User can use 4 commands in the program:
#### build
Crawls the website, builds index and saves results to file "index.json" inside the data folder

Called with:

    > build

Will print each page the crawler is currently in and return

    Crawled Website, and Saved Index of Page
    
#### load
Loads the index system from the file sytsem, required to use the print and find commands, UNLESS the user has built the index

Called with:

    > load
Returns

    Index Loaded
#### print "word"
Prints the inverted index for a word, returning the page, frequency and position said word
Example of Usage:

    > print nonsense
Returns

    Results for term: nonsense
      -Page: https://quotes.toscrape.com/page/2/
      Frequency: 1
      Position: 411
      
      -Page: https://quotes.toscrape.com/page/7/
      Frequency: 1
      Position: 279

#### find "phrase"
Finds a given phrase in the index system, returning list of all pages that contain the words in the query
Example of Usage:

    > find good friends
Returns

    Pages shared for phrase: good friends
    
      -https://quotes.toscrape.com/page/2/
      -https://quotes.toscrape.com/page/6/


## Installation and Setup

Install the requirement from the file "requirments.txt" witht

    pip install -r requirements

Run the program inside the src folder by navigating to it and running:

    python3 main.py

Should then be greated with shell interface:

    Welcome to Web Crawler - How to Use:
    
        build - crawl website, build and save index of website
    
        load - loads the index file, requires 'build' to be ran first
    
        print <word> - prints the index for a particular word
    
        find <phrase> - finds a given phrase in index
    
        close - exit crawler


## Testing Setup

Testing uses unittest, and must be called from the root file and not the src file

Use the command:

    python -m unittest discover -s tests -p "test_*.py"

This will run the 14 tests performed on the function used in the program
