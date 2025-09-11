# v₅(1000!) = ⌊1000/5⌋ + ⌊1000/25⌋ + ⌊1000/125⌋ + ⌊1000/625⌋
#           = 200 + 40 + 8 + 1 = 249

def zeros(n):
    count = 0
    for i in range(5, n + 1, 5):
        while i % 5 == 0:
            count += 1
            i = i // 5

    return count
