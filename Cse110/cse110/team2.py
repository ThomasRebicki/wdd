import math
t = float(input('insert time'))

m = float(input('insert mass'))

g = float(input('insert gravity'))

C = float(input('insert drag'))

A = float(input("insert area"))

p = float(input("insert fluid density"))

c = (1 / 2) * p * A * C


v = math.sqrt((m*g)/c) * (1- math.exp((-math.sqrt(m*g*c)/m)*t))

print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")