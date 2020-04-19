a = int(input())
cnt = 0
for x in range(1,int(a**0.5)+1):
    if a % x == 0 and a / x == x:
        cnt=cnt+1
    elif a%x==0:
        cnt=cnt+2
print(cnt)