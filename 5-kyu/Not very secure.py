# kata: https://www.codewars.com/kata/526dbd6c8c0eb53254000110
import re
def alphanumeric(password: str) -> bool:
    regex = "^[a-zA-Z\d]{1,}$"
    res = re.match(regex, password)
    print(res)
    if res:
        return True
    else:
        return False
