import math

def count_password_combinations(m):
    n = 25  # Кількість можливих символів
    combinations = math.factorial(n) // math.factorial(n - m)
    return combinations

# Припустимо, що номер студента у журналі - це m
m = 42  # Наприклад

# Обчислюємо кількість можливих комбінацій
result = count_password_combinations(m)

print("Кількість можливих комбінацій для пароля з {} комірок: {}".format(m, result))
