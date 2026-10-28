"""
Lab work calculus
"""

# A1

import numpy as np
import matplotlib.pyplot as plt

STUDENT_ID = 2
ASSIGNED_FUNCTION = STUDENT_ID % 5 + 1
print(f"+++ Номер функції: {ASSIGNED_FUNCTION} +++")

f = lambda x: np.sin(x) + x/2

a, b = 0.0, np.pi
x_values = np.linspace(a, b, 400)
y_values = f(x_values)

x_extreme = 2 * np.pi / 3
y_extreme = f(x_extreme)

plt.figure(figsize=(10, 10))
plt.plot(x_values, y_values, label=r'$f(x) = \sin(x) + \frac{x}{2}$', color = 'red')
plt.plot(x_extreme, y_extreme, 'ro',
label=f'Max $x^* = \\frac{{2\\pi}}{{3}} \\approx {x_extreme:.4f}$')
plt.title('Func graph and extreme point')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# A2

df_exact = lambda x: np.cos(x) + 1/2
df_forward =  lambda x, h: (f(x + h) - f(x))/ h
df_central = lambda x, h: (f(x + h) - f(x - h)) / (2 * h)

H = 0.0000001

err_for = abs(df_exact(x_values) - df_forward(x_values, H))
err_cent = abs(df_exact(x_values) - df_central(x_values, H))

max_err_for = np.max(err_for)
max_err_cent = np.max(err_cent)

print(f'Похибка для центральної різниці: {max_err_cent:.6e}')
print(f'Похибка для скінченних різниць: {max_err_for:.6e}')
# Df central more precise so we will be using it later

# A3

d2f_central = lambda x, h: (f(x + h) - 2 * f(x) + f(x - h)) / h**2

# A4

df = lambda x: df_central(x, 1e-6)

left, right = a, b
TOL = 1e-8
iterations_bisection = 0

while (right - left) / 2 > TOL:
    iterations_bisection += 1

    c = (left + right) / 2

    if abs(df(c)) < TOL:
        break

    if df(left) * df(c) < 0:
        right = c
    else:
        left = c


x_bisection = (left + right) / 2
print(f"Бісекція: x = {x_bisection}, ітерацій: {iterations_bisection}")
