k = int(input())
t = int(input())
t = t % (2 * k)
if t <= k:
    print(t)
else:
    print(2 * k - t)
