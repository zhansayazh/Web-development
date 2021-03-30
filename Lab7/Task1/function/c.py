n = list(map(int, input().split())) 
a = n[0]
b = n[1]
def xor(x, y):
    return x != y
print(int(xor(a,b)))