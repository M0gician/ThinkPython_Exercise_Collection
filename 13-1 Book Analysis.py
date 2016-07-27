import string
fin = open('A Tale of Two Cities.txt')

def cut_extra(fin):
    word = []
    for line in fin:
        word_list = line.split()
        for item in word_list:
            new_word = item.strip(string.punctuation)
            new_word = new_word.lower()
            word.append(new_word)
    return word
        # for letter in string.punctuation:
        #     line = line.replace(letter,'')
        #     line = line.lower()
        # word_list = line.split()
    #     if word_list != []:
    #         for item in word_list:
    #             word.append(item)
    # return word

def histogram(list):
    d = dict()
    for item in list:
        d[item] = d.get(item, 0) + 1
    return d

def find_max(d):
    t = []
    for key, value in d.items():
        t.append((value, key))

    t.sort(reverse = True)
    print 'The most common words are:'
    for freq, word in t[0:10]:
        print word, '\t', freq
    return t


def word_count(d):
    total = sum(d.values())
    print 'Total number of words:'
    print total
    return total

d = histogram(cut_extra(fin))
find_max(d)
word_count(d)


