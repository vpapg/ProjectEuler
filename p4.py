m = 0
for i in range(100,1000):
    for j in range(1000, 100, -1):
        t = i*j
        s = str(t)
        if s == s[::-1] and t>m:
            m=t
print(m)