# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

received_number = (input(f"Введите число: "))
numbers_sum = 0
for i in received_number:
    numbers_sum += int(i)
print("Сумма всех чисел: {}".format(numbers_sum))
