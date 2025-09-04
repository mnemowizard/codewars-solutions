# kata: https://www.codewars.com/kata/54b724efac3d5402db00065e
# MORSE_CODE - Только на сайте (Это словарь с расшифровкой)
from preloaded import MORSE_CODE

def decode_morse(morse_code):
    res = ""
    sentence = morse_code.strip().split('   ')
    for i in sentence:
        for j in i.split(' '):
            res += MORSE_CODE[j]
        res += ' '
    else:
        res = res[0:-1]

    return res