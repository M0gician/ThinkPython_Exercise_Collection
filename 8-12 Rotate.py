def rotate_word(word, n):
    word_old = word
    word_rot = ''
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = alphabet_lower.upper()

    for letter in word_old:
        if letter.islower():
            index = alphabet_lower.find(letter)
            index += n
            if index > 25:
                index -= 25
            word_rot += alphabet_lower[index]
        elif letter.isupper():
            index = alphabet_upper.find(letter)
            index += n
            if index > 25:
                index -= 25
            word_rot += alphabet_upper[index]
        else:
            print "Error! Please enter a word with pure letters."
            return

    print word_rot

rotate_word("MeLoN", -10)
rotate_word("M@gic", -10)
rotate_word("M0gician", -10)


