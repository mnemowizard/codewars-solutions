def longest_consec(strarr, k):
    len_arr = len(strarr)
    if len_arr == 0 or k > len_arr or k <= 0:
        return ""
    print(strarr[5:8])
    return max((''.join(strarr[i:i+k]) for i in range(len(strarr))), key=len)


print(longest_consec(["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2))



