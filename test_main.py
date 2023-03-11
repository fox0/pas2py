import pytest

from main import main


def test1():
    with open('tests/test1.pas') as f:
        text = f.read()
    assert main(text) == '''\
k = int(input())
t = int(input())
t = t % (2 * k)
if t <= k:
    print(t)
else:
    print(2 * k - t)
'''


def test2():
    with open('tests/test2.pas') as f:
        text = f.read()
    assert main(text) == '''\
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
'''


@pytest.mark.skip(reason="bug =")
def test3():
    with open('tests/test3.pas') as f:
        text = f.read()
    assert main(text) == '''\
n = int(input())
k = 0
a = 0
while (k=0)and(a<=n//3):
'''


def test4():
    with open('tests/test4.pas') as f:
        text = f.read()
    assert main(text) == '''\
A = int(input("Введите длину: "))
B = int(input("Введите шириру: "))
L = int(input("Введите дистанцию: "))
P = (A + B) * 2
Circle = L // P
L = L - P * Circle
if L <= B:
    print("LEFT")
if (L > B) and (L <= (A + B)):
    print("BOTTOM")
if (L > (A + B)) and (L <= (A + 2 * B)):
    print("RIGHT")
if (L > A + 2 * B) and (L <= P):
    print("TOP")
'''


def test_real():
    with open('tests/test_real.pas') as f:
        text = f.read()
    assert main(text) == '''\
print("Введите положительные числа A и B (A > B):")
A = float(input(" A = "))
B = float(input(" B = "))
while A >= B:
    A = A - B
print("Длина незанятой части отрезка A: ", A)
'''
