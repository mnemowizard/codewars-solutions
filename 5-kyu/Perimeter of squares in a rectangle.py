# kata: https://www.codewars.com/kata/559a28007caad2ac4e000083
def perimeter(n):
    peri_sum = 0
    fibonacci = [1,1]
    f = 0
    while f != n:
        f += 1
        peri_sum += fibonacci[0]
        fibo_sum = sum(fibonacci)
        fibonacci = [fibonacci[1], fibo_sum]
    else:
        return 4*(peri_sum + fibonacci[0])

