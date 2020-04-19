vowels = ['A', 'E', 'I', 'O', 'U']
s = raw_input()
a = 0
b = 0
for i, c in enumerate(s):
    if c in vowels:
        b += len(s) - i
    else:
        a += len(s) - i
        
if a == b:
    print "Draw"
elif a > b:
    print 'Stuart {}'.format(a)
else:
    print 'Kevin {}'.format(b)