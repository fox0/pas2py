print("Введите положительные числа A и B (A > B):")
A = float(input(" A = "))
B = float(input(" B = "))
while A >= B:
    A = A - B
print("Длина незанятой части отрезка A: ", A)
