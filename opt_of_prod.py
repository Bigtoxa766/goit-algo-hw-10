from pulp import LpMaximize, LpProblem, LpVariable, lpSum

model = LpProblem(name='maximize_production', sense=LpMaximize)

x_lemonade = LpVariable(name='Lemonade', lowBound=0, cat='Integer')
x_fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat='Integer')

model += x_lemonade + x_fruit_juice, "Total Production"

model += (2 * x_lemonade +1 * x_fruit_juice <= 100), "Water Constraint"
model += (1 * x_lemonade <= 50), "Sugar Constraint"
model += (1 * x_lemonade <= 30), "Lemon Juice Constraint"
model += (2 * x_fruit_juice <= 40), "Fruit Puree Constraint"

model.solve()

print("Оптимальне значення:")
print(f"Лимонад: {x_lemonade.value()} одиниць")
print(f"Фруктовий сік: {x_fruit_juice.value()} одиниць")
print(f"Загальна кількість продуктів: {x_lemonade.value() + x_fruit_juice.value()} одиниць")