# kata: https://www.codewars.com/kata/525c65e51bf619685c000059
def cakes(recipe, available):
    my_cakes = []
    for ing, amount in recipe.items():
        if ing in available:
            if available[ing] - amount >= 0:
                my_cakes.append(available[ing] // amount)
            else:
                return 0
        else:
            return 0

    return min(my_cakes)