def triangular(n):
    if n > 0:
        n = n * (n + 1) // 2
        return n
    else:
        return 0