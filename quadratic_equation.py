'''
Source code from:
https://www.codingeek.com/python-examples/solve-quadratic-equation/
'''

#Python program to solve quadratic equation using formula
import math


def roots_of_equation(a, b, c):

  # Finding the value of Discriminant
  D = b*b - 4*a*c
  # other way, D = b**2 - 4*a*c

  sqrt_D = math.sqrt(abs(D))

  # checking Discriminant condition
  if D > 0:
    print("Roots are Real and Different ")
    print((-b + sqrt_D)/(2*a))
    print((-b - sqrt_D)/(2*a))
  elif D == 0:
    print("Real and same roots")
    print(-b / (2*a))
  else:
  # Discriminant < 0 follows else block
    print("Complex Roots")
    print(- b / (2*a), " + i", sqrt_D)
    print(- b / (2*a), " - i", sqrt_D)



a = 1
b = 4
c = 3
# We can ask the user for value for a, b, c

# If a is given 0, then Equation is incorrect
if a == 0:
  print("The value of 'a' can not be zero. Input correct quadratic equation.")
else:
  roots_of_equation(a, b, c)
