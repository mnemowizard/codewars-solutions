# kata: https://www.codewars.com/kata/54ff3102c1bad923760001f3
def get_count(sentence):
    return sum([sentence.count('a'),sentence.count('e'), sentence.count('i'), sentence.count('o'), sentence.count('u')])