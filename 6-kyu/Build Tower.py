# kata: https://www.codewars.com/kata/576757b1df89ecf5bd00073b/solutions/python
def tower_builder(n_floors):
    pyramid = []
    for i in range(n_floors):
        pyramid.append(str('*'*(  (i)*2 + 1 )).center( (n_floors-1)*2 + 1 , ' '))
    return pyramid