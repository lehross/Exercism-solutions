import re

def is_isogram(string):
    #lowercase string and replace spaces and hyphens
    rg = "[\s-]"
    string = re.sub(rg, "", string.lower())

    return len(set(string)) == len(string)

    
    #older solution

    # for i, char in enumerate(string):
    #     if char in string[i + 1:]:
    #         return False
    
    # return True