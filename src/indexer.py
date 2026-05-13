# TAKE QUOTES FROM EACH PAGE AND BUILD "INVERTED INDEX" 
# SHOWS WHICH WORD APPEARS ON WHICH PAGE, HOW OFTEN AND WHERE
import re

# 1. RECEIVE CRAWLER
    # takes dictionary as input

# 2. TOKENISE THE TEXT/ SPLIT THE WORD AND STORE AS LOWER CASE
    # ENSURES CASE SENSITIVITY
def tokenise(text):
    words = re.findall(r"\b\w+\b", text.lower())
    return words

# 3. BUILD INVERTED INDEX
    # STORES STATS LIKE FREQUENCY, POSITION ECT. OF EACH WORD IN EACH PAGE
    # MUST BE CREATED BY THE TOOL AS IT CRAWLS THE PAGES OF THE WEBSITES
def build_indexer(pages):
    index = {}
    for page in pages:
        url = page["page"]
        text = page["text"]
        word = tokenise(text)
        for position, word in enumerate(word):
            if word not in index:
                index[word] = {}
            if url not in index[word]:
                index[word][url] = {"frequency": 0, "positions": []}

            index[word][url]["frequency"] += 1
            index[word][url]["positions"].append(position)

    return index