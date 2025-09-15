from timer_decorator import timer

@timer
def loop_for_enumerate(lst):
    for i, d in enumerate(lst):
        for j, e in enumerate(lst):
            pass

@timer
def loop_for_range(lst):
    for i in lst:
        for j in lst:
            pass


lst = [1]*1000
loop_for_range(lst)
loop_for_enumerate(lst)