def reverse(s):
    a = ""
    for i in range(len(s)-1, -1, -1):
        a = a + s[i]
    return a


def first_letter(s):
    return s[0]


def last_letter(s):
    return s[str(len(s)-1)]


