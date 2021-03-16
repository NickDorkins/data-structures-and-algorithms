from repeated_word.hashtable import Hashtable

def repeated_word(string):
    hash = Hashtable()
    words = string.split()
    print(words)

    if len(string) <= 1:
        return "Must have more than one word to have repeat values"

    for word in words:
        if hash.contains(word) is True:
            return word
        elif hash.contains(word) is False:
            hash.add(word, 1)

print(repeated_word('Hello, I am person. I am not robot.'))
