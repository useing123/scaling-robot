n = int(input())
fib_number = 0
f0 = 0
f1 = 1
counter = 0

while (counter != n):
    # print(fib_number)
    fib_number = f0 + f1
    f0 = f1
    f1 = fib_number
    counter += 1
print(f0)
