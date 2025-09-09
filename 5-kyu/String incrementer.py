# kata: https://www.codewars.com/kata/54a91a4883a7de5d7800009c
def increment_string(string):
    end_nums = ''
    start_index = None
    for i , d in enumerate(string):
        if not d.isdigit():
            end_nums = ''
        else:
            if end_nums == '':
                start_index = i
            end_nums += d
    else:
        if end_nums == '':
            end_nums = '1'
        else:
            end_nums = str(int(end_nums) + 1).rjust(len(end_nums), '0')

    return string[0:start_index] + end_nums
