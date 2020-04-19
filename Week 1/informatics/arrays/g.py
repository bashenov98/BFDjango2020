n = int(input())
c = input()
arr = c.split(" ")
ex = 0
for x in range(int(n/2)):
    ex = int(arr[x])
    arr[x] = arr[n-x-1]
    arr[n-x-1] = ex
for x in range(n):
    print(arr[x], end=" ")