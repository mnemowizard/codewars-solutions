# kata: https://www.codewars.com/kata/5544c7a5cb454edb3c000047/python
def bouncing_ball(h, bounce, window):
    if h <= 0 or not 0 < bounce < 1 or window >= h:
        return -1

    return sum(1 if bounce**(i+1)*h == window else 2 for i in range(int(h)) if bounce**(i+1)*h > window) + 1