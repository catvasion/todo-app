meals = ['shoes', 'shirts', 'jeans']
meals.sort()

for index, meal in enumerate(meals):
    row = f"{index+1}.{meal.capitalize()}"
    print(row)