s = raw_input().strip()
k = int(raw_input())
i = 0
while i < len(s):
    a = s[i:i+k]
    output = ""
    for x in a:
        if x not in output:
            output += x
    print output
    i += k