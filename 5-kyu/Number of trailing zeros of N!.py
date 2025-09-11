# kata: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
def zeros(n):
    count = 0
    for i in range(5, n + 1, 5):
        while i % 5 == 0:
            count += 1
            i = i // 5

    return count

print(zeros(1000))
print(zeros(1000000000))
