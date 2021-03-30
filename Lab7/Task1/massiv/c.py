n = int(input())
cnt  = 0
a = list(map(int, input().split())) 
for i in range(len(a)):
    if(a[i] > 0):
        cnt = cnt + 1
print(cnt)