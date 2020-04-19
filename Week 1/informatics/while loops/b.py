n = int(input())
x = 2
while(x != n + 1):
    if n % x == 0:
        print(x)
        break
    x = x + 1
    continue
