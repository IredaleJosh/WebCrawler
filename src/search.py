# PRINT INVERTED INDEX FOR A WORD
# FIND QUERY PHRASE AND RETURN LIST OF ALL PAGES CONTAINING IT

def print_word(index, word):
    if not isinstance(word, str):
        return {}
    word = word.lower()
    return index.get(word, {})

def find_word(index, query):
    # MUST BE A LIST
    if not isinstance(query, list):
        return []
    # SPLIT THE QUERY
    words = []
    for word in query:
        if isinstance(word, str):
            phrase = word.strip().lower()
            if phrase:
                words.append(phrase)
    # EMPTY STRINGS
    if not words:
        return []
    # STORE PAGES
    sets = []
    for word in words:
        if word in index:
            sets.append(set(index[word].keys()))
        else:
            return []
    return list(set.intersection(*sets))