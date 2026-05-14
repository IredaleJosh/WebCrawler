# TAKE QUOTES FROM EACH PAGE AND BUILD "INVERTED INDEX" 
# SHOWS WHICH WORD APPEARS ON WHICH PAGE, HOW OFTEN AND WHERE
import re

# TOKENISE THE TEXT/ SPLIT THE WORD AND STORE AS LOWER CASE
def tokenise(text):
    if not isinstance(text, str):
        return []
    words = re.findall(r"\b\w+\b", text.lower())
    return words

# BUILD INVERTED INDEX
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