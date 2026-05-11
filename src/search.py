# PRINT INVERTED INDEX FOR A WORD
# FIND QUERY PHRASE AND RETURN LIST OF ALL PAGES CONTAINING IT

def print_word(index, word):
    word = word.lower()
    return index.get(word, {})

def find_word(index, query):
    words = query.lower().split()
    sets = []
    for word in words:
        if word in index:
            sets.append(set(index[word].keys()))
        else:
            return []
    return list(set.intersection(*sets))