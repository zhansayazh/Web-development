n = int(input())
cnt  = 0
a = list(map(int, input().split())) 
for i in range(len(a)-1):
    if(a[i+1] > 0 and a[i] > 0 or a[i+1] < 0 and a[i] < 0):
        cnt = cnt + 1
if(cnt > 0):
    print('YES')
else:
    print('NO')
