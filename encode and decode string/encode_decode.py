def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return s


