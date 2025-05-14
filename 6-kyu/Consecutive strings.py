# kata: https://www.codewars.com/kata/56a5d994ac971f1ac500003e/solutions/python
def longest_consec(strarr, k):
    res = ''
    merge = ''
    d = []
    if k <= 0 or len(strarr) < k:
        return ''

    for i in range(len(strarr) - k + 1):
        for j in range(k):
            merge += strarr[i + j]
        d.append(merge)
        merge = ''

    return sorted(d, key=len, reverse=True)[0]