# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
print(pi)
d = float(input("Введите число для заданной точности числа Пи: (Пример: 0.001) "))
for i in range(1, 16):
    if d < 1:
        d = d*10
        # print("d=", d, "i=", i)
        x = i
print("Число Пи с заданной точностью: ", round(pi, x))