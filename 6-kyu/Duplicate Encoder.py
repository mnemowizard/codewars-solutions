# kata: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
def duplicate_encode(word: str):
    lower_word = word.lower()
    res = ''.join(map( lambda char: '(' if lower_word.count(char) == 1 else ')', lower_word))
    return res