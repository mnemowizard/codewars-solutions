# kata : https://www.codewars.com/kata/56747fd5cb988479af000028
def get_middle(s):
    s_len = len(s)
    return s[s_len//2] if s_len%2 !=0 else s[s_len//2-1] + s[s_len//2]