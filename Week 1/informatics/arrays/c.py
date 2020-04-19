n = int(input())
c = input()
arr = c.split(" ")
cnt = 0
for x in range(n):
    if int(arr[x]) > 0:
        cnt = cnt + 1
print(cnt)
