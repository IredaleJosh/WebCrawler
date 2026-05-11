from crawler import crawl_site
from indexer import build_indexer
import json
import sys
import os

# SAVE TO JSON FILE
def save_as_index(indexed, filename="index.json"):
    with open(filename, "w") as f:
        json.dump(indexed, f)

# LOAD THE JSON FILE
def load_index(filename="index.json"):
    if not os.path.exists(filename):
        print("No index found: Please run 'build' before using 'load'")
    with open(filename, "r") as f:
        return json.load(f)

# MAIN - CHECKS CMD
def main():
    # CCONFIRM CMD IS SAVED
    if len(sys.argv) < 2:
        print("Please use commands")
        print("build - crawl website, build index and save resulting index") 
        print("load - loads the index file, requires 'build' to be ran first")
        return
    cmd = sys.argv[1]

    if cmd == "build":
        # CRAWL THE PAGES + INDEX + SAVE
        pages = crawl_site("https://quotes.toscrape.com")
        indexed =  build_indexer(pages)
        save_as_index(indexed)
        print("CRAWLED, INDEXED AND SAVED")

    if cmd == "load":
        indexed = load_index()
        if indexed is None:
            return
        else:
            print("LOAD INDEXD PAGES")

    # if cmd == "print":



# Main Function
if __name__ == "__main__":
    main()

