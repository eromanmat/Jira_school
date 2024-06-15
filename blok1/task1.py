

# Дана сторона квадрата a. Найти его периметр P = 4·a

a = int(input("Enter side: "))

num = 4
p = num * a

print(p)


# Дана сторона квадрата a. Найти его площадь{{ S = a2}}

a = int(input("Enter side: "))

s = num**2

print(s)

# Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)

a = int(input("Enter side: "))
b = int(input("Enter side: "))

s = a * b
p = 2 * (a + b)

print(s)
print(p)

# Дан диаметр окружности d. Найти ее длину{{ L = π·d, π = 3.14}}

d = int(input("Enter side: "))

p = 3.14
l = p * d

print(l)

# Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6·a2

a = int(input("Enter side: "))

v = a**3
s = 6  * a**2

print(v)
print(s)
# Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)

a = int(input("Enter side: "))
b = int(input("Enter side: "))
c = int(input("Enter side: "))

v = a * b * c
s = 2 * (a * b + b * c + a * c)

print(v)
print(s)

# Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2, π=3.14

r = int(input("Enter side: "))

p = 3.14

l = 2 * p * r
s = p * r**2

print(l)
print(s)

# Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2

a = int(input("Enter side: "))
b = int(input("Enter side: "))

c = (a + b)/2

print(c)

# Даны два неотрицательных числа a и b. Найти их среднее геометрическое, т. е. квадратный корень из их произведения: (a·b)1/2

a = int(input("Enter side: "))
b = int(input("Enter side: "))

с = (a * b) * 1/2

print(c)

# Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.

a = int(input("Enter side: "))
b = int(input("Enter side: "))

a_squared = a ** 2
b_squared = b ** 2

sum_of_squares = a_squared + b_squared

difference_of_squares = a_squared - b_squared

product_of_squares = a_squared * b_squared

quotient_of_squares = a_squared / b_squared 

print("Sum of their squares:", sum_of_squares)
print("Difference of their squares:", difference_of_squares)
print("Product of their squares:", product_of_squares)
print("Quotient of their squares:", quotient_of_squares)