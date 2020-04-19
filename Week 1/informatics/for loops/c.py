a = int(input())
b = int(input())
for x in range(a, b+1):
    y=int(x**0.5)
    if y*y==x:
        print(x)