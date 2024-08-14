# You will be given a number and you will need to return it as a string in Expanded Form

# Test Cases:
# 70304 -> '70000 + 300 + 4'
# 42 -> '40 + 2'
# 710163 -> '700000 + 10000 + 100 + 60 + 3'
# 853546 -> '800000 + 50000 + 3000 + 500 + 40 + 6'
# 511604 -> '500000 + 10000 + 1000 + 600 + 4'

def Expanded(num):
    strnum = str(num)
    lennum = len(num)
    listn = []
    for i,x in enumerate(strnum):
        if x != 0:
            value = int(x) * (10 ** (lennum - i -1))
            listn.append(str(value))
    return "+".join(listn)

print(Expanded("710163"))