import sys

a = int(input())
n = int(input())
# f = 0
number = 0
sys.set_int_max_str_digits(10000)
power = 1
for i in range(0, n+1):
    number += power
    power *= a
print(number)
