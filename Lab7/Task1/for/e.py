a = int(input())
cnt = 0
while(a != 0):
    b = a % 10
    cnt = cnt + b
    a = a // 10
print(cnt)