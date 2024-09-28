n = int(input())

answer = 0
answer_x = 0
answer_y = 0
for i in range(n):
    x, y = map(int, input().split())
    x = abs(x)
    y = abs(y)
    c = (x*x)+(y*y)
    if (c > answer):
        answer = c
        answer_x = x
        answer_y = y
print(answer_x, answer_y)
