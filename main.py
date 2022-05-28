# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as f:
        return str(f.read().splitlines())

import string
def count_words():
    text = read_file_content("./story.txt")
    mapp = text.marketrans(string.punctuation, " "*32)
    ff = text.translate(mapp)
    text_list = ff.split

    return {i:text_list.count(i) for i in set(text_list)}
