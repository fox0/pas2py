n = int(input())
k = 0
a = 0
while (k=0)and(a<=n//3):
    b = 0
    while (k=0)and(b<=n//5):
        if 3*a+5*b=n:
            print(a,' ',b)
            k = k+1
        b = b+1
    a = a+1
if k=0:
    print('IMPOSSIBLE')
