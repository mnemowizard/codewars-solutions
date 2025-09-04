# kata: https://www.codewars.com/kata/52685f7382004e774f0001f7
def make_readable(seconds: int):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return str(hours).rjust(2, '0') + ':' + \
            str(minutes).rjust(2, '0') + ':' + \
            str(seconds).rjust(2, '0')

print(make_readable(359999))