# kata : https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
def duplicate_count(text: str):
    text_lower = text.lower()
    was_chars = []
    counter = 0
    for i in text_lower:
        if text_lower.count(i) > 1 and i not in was_chars:
            was_chars.append(i)
            counter += 1
    return counter

