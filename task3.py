n = 0
a = int(input())
number = 2
temp_number = 0
while (temp_number < a):
    temp_number = number ** n
    n += 1
    if temp_number < a:
        print(temp_number)
    elif (temp_number == a):
        print(temp_number)
    else:
        break
