# kata: https://www.codewars.com/kata/54ba84be607a92aa900000f1
def is_isogram(string: str):
    return all(string.lower().count(char) == 1 for char in string.lower())


