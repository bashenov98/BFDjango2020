n = int(input())
x = 1
while(x != n + 1):
    if int(x**0.5)*int(x**0.5) == x:
        print(x)
    x = x + 1
    continue
