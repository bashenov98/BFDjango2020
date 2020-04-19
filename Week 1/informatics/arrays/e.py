n = int(input())
c = input()
arr = c.split(" ")
cnt = 0
for x in range(1, n):
    if int(arr[x]) * int(arr[x-1]) > 0:
        cnt = 1
if cnt == 1:
    print('YES')
else:
    print('NO')
