


#Часть 4. Списки


# Используя операции индексирования и среза выведите на экран первый и третий элементы списка [1, 2, 3 ,4 ,5],
# а также срез списка из первых трех элементов.

# numbers = [1, 2, 3 ,4 ,5]
# print(numbers[0], numbers[2])
# print(numbers[:3])

# Дан список [«Ростов», «+», «на», «-», «Дону»]. Исправьте плюс на дефис и выведите название города на экран
#  использовав доступ к элементам списка по индексам

# list_items = ['Ростов', '+', 'на', '-', 'Дону']
# list_items[1] = '-'
# print(list_items[0], list_items[1], list_items[2], list_items[3], list_items[4])


# Дан список [«a», «s», «1», «a», «32», «23»]. Разбейте его на два списка: только с буквами и только с числами. 

# list_items = ['a', 's', '1', 'a', '32', '23']
# list_numbers = []
# list_str = []

# for item in list_items:
#     if item.isdigit():
#         list_numbers.append(item)
#     else:
#         list_str.append(item)

# print(list_numbers)
# print(list_str)


# В предыдущей задаче должен был получиться список из букв. Используя методы списков: 
# удалите из него последний элемент, сделайте реверсию списка.

# list_items = ['a', 's', 'a']

# del list_items[-1]
# list_items.reverse()

# print(list_items)

# Преобразуйте список [«a», «s», «1», «a», «32», «23»] в set и выведите на экран. Что изменилось?

# list_items = ['a', 's', '1', 'a', '32', '23']

# set_items = set(list_items)

# print(set_items)



