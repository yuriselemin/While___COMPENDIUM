
# Цикл for
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Цикл while
i = 0
while i < 5:
    print(i)
    i += 1

# Цикл continue
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# Цикл break
for num in range(10):
    if num == 5:
        break
    print(num)

# Цикл pass
for num in range(10):
    pass

# Цикл else для for
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
else:
    print("Все числа меньше 3")

# Цикл with
with open('example.txt', 'w') as file:
    file.write('Пример текста')

# Цикл try-except
try:
    1 / 0
except ZeroDivisionError:
    print("Деление на ноль недопустимо")

# Цикл try-finally
try:
    raise Exception('Ошибка')
finally:
    print("Блок finally выполняется всегда")

# Цикл itertools
from itertools import count
for i in count(1):
    if i > 5:
        break
    print(i)

# Пример 1: Бесконечный цикл
i = 42
while True:
    print(i)
    i -= 1
    if i == -1:
        break

# Пример 2: Чтение числа до ввода корректного
while True:
    try:
        number = int(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка: введенное значение не является числом.")

# Пример 3: Обработка файла построчно
with open('example.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())

# Пример 4: Запрос у пользователя до получения положительного ответа
while True:
    answer = input("Хотите продолжить? (y/n)")
    if answer.lower() == 'y':
        break

# Пример 5: Генератор случайных чисел
import random
while True:
    print(random.randint(1, 10))




















