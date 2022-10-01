# Напишите программу, которая принимает на вход число
#  N и выдает
# набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

received_number = (input(f"Введите число: "))
a = []
i = 0
while i < (int(received_number)):
    numbers_sum = 1
    o = 0
    i += 1
    while o < (int(received_number)):
        o += 1
        numbers_sum *= o
        if (i == (int(received_number))):
            a.append(numbers_sum)
print(a)
