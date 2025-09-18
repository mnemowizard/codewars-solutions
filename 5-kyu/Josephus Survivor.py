# kata: https://www.codewars.com/kata/555624b601231dc7a400017a
def josephus_survivor(n,k):
    circle = list(range(1,n+1))
    index = 0
    while len(circle) != 1:
        index = (index + k - 1) % len(circle) if len(circle) else len(circle)
        circle.pop(index)

    return circle[0]


