

# Часть 2. Все входные и выходные данные в заданиях этой группы являются целыми числами.
# Все числа, для которых указано количество цифр (двузначное число, трехзначное число и т. д.), считаются положительными.



# Дано расстояние L в сантиметрах. Используя операцию деления нацело, найти количество полных метров в нем (1 метр = 100 см).

# l = int(input("Enter side: "))
# m = l//100
# print(m)

# Дана масса M в килограммах. Используя операцию деления нацело, найти количество полных тонн в ней (1 тонна = 1000 кг).

# m = int(input("Enter side: "))
# kg = m//1000
# print(kg)

# Дан размер файла в байтах. Используя операцию деления нацело, найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта).

# byte = int(input("Enter side: "))
# kilobyte = byte//1024
# print(kilobyte)

# Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
#  Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.

# a = int(input("Enter side: "))
# b = int(input("Enter side: "))

# if a > b:
#     quantity = a // b
#     print(quantity)
# else:
#     print("Error: A must be greater than B")


# Даны целые положительные числа A и B (A > B). На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений). 
# Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.

# a = int(input("Enter side: "))
# b = int(input("Enter side: "))

# if a > b:
#     remainder = a % b
#     print(remainder)
# else:
#     print("Error: A must be greater than B")

# Дано двузначное число. Вывести вначале его левую цифру (десятки), а затем — его правую цифру (единицы).
# Для нахождения десятков использовать операцию деления нацело, для нахождения единиц — операцию взятия остатка от деления.

# number = int(input("Enter side: "))

# tens = number // 10
# units = number % 10

# print(f"In the {number}:\nTens: {tens}\nUnits: {units}")
 
# Дано двузначное число. Найти сумму и произведение его цифр.

# number = int(input("Enter side: "))

# tens = number // 10
# units = number % 10

# number_sum = tens + units
# number_multiplication = tens * units
# print(f"sum of numbers = {number_sum}")
# print(f"multiplying numbers = {number_multiplication}")

# Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.

# number = int(input("Enter side: "))

# tens = number // 10
# units = number % 10

# number_sum = str(units) + str(tens)
# print(int(number_sum))

# Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни).

# number = int(input("Enter side: "))

# hundreds = number // 100

# print(hundreds)

# Дано трехзначное число. Вывести вначале его последнюю цифру (единицы), а затем — его среднюю цифру (десятки).

# number = int(input("Enter side: "))

# units = number % 10
# tens = (number // 10) % 10

# print(units)
# print(tens)
