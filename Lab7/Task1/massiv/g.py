n = int(input())
a = list(map(int, input().split())) 
for i in range(len(a)//2):
    b = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = b
for i in range(len(a)):
    print(a[i])