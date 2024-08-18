def encode(st):
    pass
    
def decod(s):
    if s == "1":
        return "a"
    if s == "2":
        return "e"
    if s == "3":
        return "i"
    if s == "4":
        return "o"
    if s == "5":
        return "u"
    if s == "a":
        return "1"
    if s == "e":
        return "2"
    if s == "i":
        return "3"
    if s == "o":
        return "4"
    if s == "u":
        return "5"
    return s
encode = decode = lambda st: ''.join(map(decod,st))