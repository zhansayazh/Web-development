n = int(input())
cnt  = 0
a = list(map(int, input().split())) 
for i in range(len(a)-2):
    if(a[i+1] > a[i] and a[i+1] > a[i+2]):
        cnt = cnt + 1
print(cnt)