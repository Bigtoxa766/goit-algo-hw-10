import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  
b = 2  

analytical_result = (b ** 3)/3 - (a ** 3)/3

num_points = 1000000
x_random = np.random.uniform(a,b,num_points)
y_random = np.random.uniform(0, b ** 2, num_points)

under_curve = y_random < f(x_random)
monte_carlo_result = (b-a)*(b**2)*np.sum(under_curve) /num_points

quad_result, _ = quad(f,a,b)

print(f"Аналітичне значення інтегралу: {analytical_result:.5f}")
print(f"Значення методом Монте-Карло: {monte_carlo_result:.5f}")
print(f"Значення методом quad: {quad_result:.5f}")

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

ax.scatter(x_random, y_random, color="blue", s=1, alpha=0.3)
plt.title(f"Метод Монте-Карло для f(x) = x^2 на інтервалі [{a}, {b}]")
plt.grid()
plt.show()
