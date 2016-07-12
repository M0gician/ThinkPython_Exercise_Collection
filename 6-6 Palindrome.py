def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome():
    word = raw_input("Please enter a word: ")
    for i in range(len(word)):
        correctness = word[i] == word[len(word) - 1 - i]
        if correctness == False:
            return False
    return correctness


print is_palindrome()
