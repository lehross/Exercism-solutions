from collections import Counter
import re

def count_words(sentence):
    pattern = r"[!@#$%^&*()_+<>?:.,;/\n\t]"
    quotes = r"'\w*'"
    
    # remove non-ASCII characters
    sentence = re.sub(pattern, " ", sentence)

    # remove quotes
    list_of_quotes = re.findall(quotes, sentence)
    sentence = re.sub(quotes, "", sentence)

    # add the words that had quotes
    sentence += "".join([re.sub("'", "", q) for q in list_of_quotes])

    # count the occurrences of each word     
    split_sentence = re.split(r"[\s*]", sentence.lower())
    return dict(Counter(x for x in split_sentence if x not in ' '))
