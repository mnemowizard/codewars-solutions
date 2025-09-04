# kata: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
def is_pangram(st):
    st_lower = st.lower()
    alphabets = list(range(ord('a'), ord('z') + 1))
    for char in st_lower:
        try:
            alphabets.remove(ord(char))
        except:
            pass

    return alphabets == []
