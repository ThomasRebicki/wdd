

from multiprocessing.connection import answer_challenge


x = input("Size of the side of the square in cm: ")
answer = int(x)**2
answer2 = int(x)**3
print(f"{answer / 100} m2")
print(f"{answer2 / 100} m3")

x = input("Size of the side of the rectangle in cm: ")
y = input("Size of the base of the rectangle in cm: ")
z = input("Size of the lenght of the rectangle in cm: ")
answer = int(x)*int(y)
answer2 = int(x)*int(y)*int(z)

print(f"{answer/ 100} m2")
print(f"{answer2/ 100} m3")

import math
x = input("radius of the circle in cm: ")
answer = (int(x)**2)* math.pi
answer2 = (4 / 3) * math.pi * (int(x) ** 3)
print(f"{answer/ 100} m2")
print(f"{answer2/ 100} m3")