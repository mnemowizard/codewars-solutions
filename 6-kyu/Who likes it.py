# kata: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
def likes(names):
    if names:
        if len(names) == 1:
            return f"{names[0]} likes this"
        elif len(names) == 2:
            return f"{names[0]} and {names[1]} like this"
        elif len(names) == 3:
            return f"{names[0]}, {names[1]} and {names[2]} like this"
        else:
            return f"{names[0]}, {names[1]} and {len(names[2:])} others like this"
    else:
        return  "no one likes this"