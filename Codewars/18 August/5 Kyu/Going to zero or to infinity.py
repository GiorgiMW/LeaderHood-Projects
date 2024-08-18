def going(n):
    num1 = 1
    num2 = 0
    for i in range(1, n + 1):
        num1 = num1 * i
        num2 = num2 + num1
    return num2 / num1