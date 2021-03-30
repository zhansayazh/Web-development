n = int(input())
cnt  = 0
a = list(map(int, input().split())) 
for i in range(len(a)-1):
    if(a[i+1] > a[i]):
        cnt = cnt + 1
print(cnt)