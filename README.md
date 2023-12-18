print("Меню:")
print("1. Шаверма")
print("2. Шаурма")
print("3. Фалафель")
print("4. Самса")

food_number = input("Введите номер блюда, которое хотите заказать: ")

if food_number == "1":
    print("Вы заказали шаверму!")
elif food_number == '2':
    print('Вы заказали шаурму!')
elif food_number == '3':
    print('Вы заказали фалафель!')
elif food_number == '4':
    print('Вы заказали самсу!')
else:
    print('Блюда с таким номером нет.')
