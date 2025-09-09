# kata: https://www.codewars.com/kata/514a024011ea4fb54200004b
def domain_name(url):
    if 'www.' in url:
        return url.split('.')[1]
    elif '//' in url:
        return url.split('//')[1].split('.')[0]
    else:
        return url.split('.')[0]