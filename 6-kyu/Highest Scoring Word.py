# kata: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
def high(x):
    words = x.split()
    highest_score = 0
    highest_word = ''
    for word in words:
        word_score = sum(map( lambda y: ord(y) - 96, word))
        if word_score > highest_score:
            highest_score = word_score
            highest_word = word

    return highest_word