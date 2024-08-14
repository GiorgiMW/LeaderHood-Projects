# Write an algorithm in python to count the number of capital letters in
# a string. How many comparisons does it do? What is the fewest num-
# ber of increments it might do? What is the largest number? (Use N for the
# number of characters in the file when writing your answer.)
def count_letters(str):
    num = 0
    for i in str:
        if i.isupper():
            num = num + 1
    return num