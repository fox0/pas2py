a = int(input())
b = int(input())
c = int(input())
n = int(input())
d = (a + b + c + n) // 4
if (a > 2 * d) or (b > d) or (c > d):
    print(0)
else:
    print(2 * d - a)
    print(d - b)
    print(d - c)
