def is_pangram(sentence):
    if sum(chr(char) in sentence.lower() for char in range(ord('a'), ord('z') + 1)) == 26:
        return True
    return False
