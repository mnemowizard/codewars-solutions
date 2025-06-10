# kata: https://www.codewars.com/kata/514b92a657cdc65150000006/python
def solution(number):
    return sum([x for x in range(number) if x % 3 == 0 or x % 5 == 0])