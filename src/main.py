from crawler import crawl_site
from indexer import build_indexer
from search import print_word, find_word
import json
import sys
import os

# SAVE TO JSON FILE
def save_as_index(indexed, filename="../data/index.json"):
    with open(filename, "w") as f:
        json.dump(indexed, f, indent=4)

# LOAD THE JSON FILE
def load_index(filename="../data/index.json"):
    if not os.path.exists(filename):
        print("No index found: Please run 'build' before using 'load'")
        return
    with open(filename, "r") as f:
        return json.load(f)

# MAIN LOOP
def program_loop():

    indexed = None

    # Explain structure
    print("""
Welcome to Web Crawler - How to Use:
    build - crawl website, build and save index of website\n
    load - loads the index file, requires 'build' to be ran first\n
    print <word> - prints the index for a particular word\n
    find <phrase> - finds a given phrase in index\n
    close - exit crawler""")

    while True:
        cmd = input("> ").strip().split()

        if not cmd:
            print("No command given. Try Agaim")
            continue

        choice = cmd[0]

        if choice == "close":
            print("Exit Program")
            break;

        elif choice == "build":
            pages = crawl_site("https://quotes.toscrape.com")
            indexed =  build_indexer(pages)
            save_as_index(indexed)
            print("Crawled Website, and Saved Index of Page")

        elif choice == "load":
            indexed = load_index()
            if indexed is None:
                continue
            else:
                print("Index Loaded")

        elif choice == "print":
            print(len(choice))
            if indexed is None:
                print("Invalid Order: Load must be called before. Try Again")
                continue
            if len(cmd) == 1:
                print("Invalid Command: Please choose a word to be printed. Try Again")
                continue
            word = cmd[1]
            result = print_word(indexed, word)
            # NICER FORMAT
            if not result:
                print(f"No results found for term: {word}")
            else:
                print(f"Results for term: {word}")
                for url, data in result.items():
                    freq = data["frequency"]
                    pos = " , ".join(str(p) for p in data["positions"])
                    print(f" -Page: {url}")
                    print(f" Frequency: {freq}")
                    print(f" Position: {pos}\n")

        elif choice == "find":
            if indexed is None:
                print("Invalid Order: Load must be called before. Try Again")
                continue
            if len(cmd) == 1:
                print("Invalid Command: Please choose a phrase to locate. Try Again")
                continue
            phrase = cmd[1:]
            result = find_word(indexed, phrase)
            print(json.dumps(result, indent=4))

        else:
            print("Unknown commands. Try Again")

# Main Function
if __name__ == "__main__":
    program_loop()
