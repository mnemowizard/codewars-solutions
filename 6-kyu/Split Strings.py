# kata: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
def solution(s):
    len_s = len(s)
    return [s[x] + s[x+1] if x != len_s - 1 else s[x] + '_' for x in range(0, len_s, 2)]

