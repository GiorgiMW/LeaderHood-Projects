def is_divisible(*s):
    for i in range(1, len(s)):
        if s[0] % s[i] != 0:
            return False
    return True