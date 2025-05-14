# kata: https://www.codewars.com/kata/546f922b54af40e1e90001da/solutions/python
def alphabet_position(text):
    alpha_pos = {x : ord(x) - 96 for x in text.lower() if ord(x) in range(97, 123)}
    res = ''
    for i in text.lower():
        if i in alpha_pos:
            res += str(alpha_pos[i]) + ' '
    return res[0:-1]

print(alphabet_position("The sunset sets at twelve o' clock."))