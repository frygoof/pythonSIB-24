# my_list = [6, "АйдосНаКиаСерато", 69.96, True, [2, 3, 1]]
#
# for element in my_list:
#     element_type = type(element)
#     print(f"Element: {element}, ElType: {element_type}")

# input_string = input("Введите элементы списка, разделенные пробелом: ")
# elements = input_string.split()
#
# my_list = [int(element) for element in elements]
#
# for i in range(0, len(my_list) - 1, 2):
#     my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
# print("Список после обмена значений соседних элементов:", my_list)

# seasons_dict = {
#     1: 'WINTER',
#     2: 'WINTER',
#     3: 'SPRING',
#     4: 'SPRING',
#     5: 'SPRING',
#     6: 'SUMMER',
#     7: 'SUMMER',
#     8: 'SUMMER',
#     9: 'AUTUMN',
#     10: 'AUTUMN',
#     11: 'AUTUMN',
#     12: 'WINTER'
# }
# month = int(input("Какой по счёту ваш месяц? (от 1 до 12): "))
# season = seasons_dict.get(month, "Месяцев всего 12")
# print(f"Месяц {month} относится к времени года: {season}")

# input_string = input("Введите строку из слов: ")
# words = input_string.split()
#
# for i, word in enumerate(words, 1):
#     print(f"{i}. {word[:10]}")

# ratings = [7, 5, 3, 3, 2]
#
# while True:
#     new_rating = int(input("Введите новый элемент рейтинга (натуральное число): "))
#     ratings.append(new_rating)
#     ratings.sort(reverse=True)
#     print("Результат:", ratings)

# products = []
# while True:
#     name = input("Введите название товара (или 'стоп' для завершения ввода): ")
#     if name == 'стоп':
#         break
#     try:
#         price = float(input("Введите цену товара: "))
#         quantity = int(input("Введите количество товара: "))
#     except ValueError:
#         print("Ошибка ввода данных. Пожалуйста, введите корректные числовые значения.")
#         continue
#     unit = input("Введите единицу измерения товара: ")
#     product = {
#         "название": name,
#         "цена": price,
#         "количество": quantity,
#         "ед": unit
#     }
#     products.append(product)
#
# analytics = {
#     "название": [],
#     "цена": [],
#     "количество": [],
#     "ед": []
# }
#
# for product in products:
#     for key, value in product.items():
#         analytics[key].append(value)
#
# if products:
#     avg_price = sum(analytics["цена"]) / len(products)
#     print("\nАналитика о товарах:")
#     print(f"Средняя цена товаров: {avg_price:.2f}")
#     for key, value in analytics.items():
#         if key != "цена":
#             unique_values = list(set(value))
#             print(f"{key}: {', '.join(map(str, unique_values))}")
# else:
#     print("Список товаров пуст.")