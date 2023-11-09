from pulp import *

# Задаем данные
m = 2  # количество полей
n = 3  # количество культур

fields = range(1, m + 1)
crops = range(1, n + 1)

ai = [10, 20]  # площади полей
aij = [[5, 3, 2], [4, 6, 1]]  # урожайность культур на полях
bj = [8, 12, 6]  # план производства культур
cj = [100, 150, 120]  # цены продукции

# Создаем переменные решения
x = LpVariable.dicts('x', [(i, j) for i in crops for j in fields], lowBound=0, cat='Continuous')

# Создаем задачу максимизации
prob = LpProblem("Profit Maximization", LpMaximize)

# Добавляем целевую функцию
prob += lpSum([aij[i - 1][j - 1] * x[(i, j)] * cj[i - 1] for i in crops for j in fields])

# Добавляем ограничения
for j in fields:
    prob += lpSum([x[(i, j)] for i in crops]) <= ai[j - 1]

for i in crops:
    prob += lpSum([x[(i, j)] for j in fields]) == bj[i - 1]

# Решаем задачу
prob.solve()

# Выводим результаты
print("Status:", LpStatus[prob.status])
print("Maximized Profit =", value(prob.objective))

for v in prob.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)
