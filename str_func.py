def reverse(s):
    a = ""
    for i in range(len(s)-1, -1, -1):
        a = a + s[i]
    return a


def firstLetter(s):
    return s[0]


