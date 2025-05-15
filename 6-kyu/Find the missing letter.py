# kata: https://www.codewars.com/kata/5839edaa6754d6fec10000a2/python
def find_missing_letter(chars):
    for d in range(len(chars) - 1):
        if ord(chars[d]) + 1 != ord(chars[d+1]):
            return chr(ord(chars[d]) + 1)