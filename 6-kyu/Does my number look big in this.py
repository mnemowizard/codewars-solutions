# kata: https://www.codewars.com/kata/5287e858c6b5a9678200083c
def narcissistic( value : int):
    value_len = len(str(value))
    narcissistic_value = lambda x: x**value_len if x < 10 else (x%10)**value_len + narcissistic_value(x//10)
    return value == narcissistic_value(value)

print(narcissistic(153))