def mini(a, b, c, d):
    print(min(min(a, b), min(c, d)))


a, b, c, d = [int(x) for x in input().split()]
mini(a, b, c, d)
