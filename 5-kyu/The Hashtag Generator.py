# kata: https://www.codewars.com/kata/52449b062fb80683ec000024
def generate_hashtag(s: str):
    split_s = s.split()
    return '#' + ''.join(i[0].upper() + i[1:].lower() if i.isalpha() else i for i in split_s) if sum(map(len, split_s)) <= 139 and s != '' else False
