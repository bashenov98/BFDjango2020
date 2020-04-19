n = int(input())
c = input()
arr = c.split(" ")
for x in range(n):
    if int(arr[x]) % 2 == 0:
        print(arr[x], end=" ")
