# Напишите программу, которая определяет наименьшее из четырёх чисел.

# Формат входных данных
# На вход программе подаётся четыре целых числа.

# Формат выходных данных
# Программа должна вывести наименьшее из четырёх чисел.

# Примечание. Учитывайте, что минимальные числа могут повторяться (cмотрите тест 5)

# code

num_1, num_2, num_3, num_4 = int(input()), int(input()), int(input()), int(input())

if num_1 > num_2:
    num_1 = num_2
if num_3 > num_4:
    num_3 = num_4
if num_1 > num_3:
    num_1 = num_3
print(num_1)
