


numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    current_number = numbers[index]
    print(f"Number at index {index}: {current_number}")
    index += 1





list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

while list1 or list2:  # Продолжаем цикл, пока хотя бы один список не пуст
        if list1 and list2 and list1[-1] == list2[-1]:  # Проверяем последний элемент каждого списка
            print(f"{list1[-1]} is in both lists")
            list1.pop()  # Удаляем последний элемент из первого списка
            list2.pop()  # Удаляем последний элемент из второго списка
        elif list1:  # Если первый список не пуст, но второй пуст
            print(f"{list1[-1]} is only in the first list")
            list1.pop()  # Удаляем последний элемент из первого списка
        else:  # Если первый список пуст, но второй нет
            print(f"{list2[-1]} is only in the second list")
            list2.pop()  # Удаляем последний элемент из второго списка





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
