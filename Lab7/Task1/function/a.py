n = list(map(int, input().split())) 
a = n[0]
b = n[1]
c = n[2]
d = n[3]
def minimum(a, b, c, d):
    return min(a, b, c, d)
print(minimum(a, b, c, d))
