def dig_pow(n, p):
    num = 0
    for i in str(n):
        num = num + int(i) ** p
        p = p + 1
    if num % n == 0:
        return num / n
    else:
        return -1