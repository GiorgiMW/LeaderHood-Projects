def rot13(message):
    listn = []
    for i in message:
        if i.isupper() == True:
            x = ord(i) + 13
            y = chr(x)
            if x > 90:
                u = x - 91
                o = chr(u + 65)
                listn.append(o)
            else:
                listn.append(y)
        elif i.islower() == True:
            j = ord(i) + 13
            k = chr(j)
            if j > 122:
                z = j - 123
                p = chr(z + 97)
                listn.append(p)
            else:
                listn.append(k)
        else:
            listn.append(i)
    return "".join(listn)
                
