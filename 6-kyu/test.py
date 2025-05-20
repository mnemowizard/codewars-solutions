# put your python code here
def get_prime():
    prime = 1
    while True:
        prime += 1
        for d in range(2, prime):
            if prime % d == 0:
                break
        else:
            yield prime


gen = get_prime()
print(next(gen))
print(next(gen))