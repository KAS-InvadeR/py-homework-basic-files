import os


cook_book = {}

with open('recipes.txt', 'rt', encoding='utf-8') as recipes_fl:
    for r in recipes_fl:
        recipes_name = r.strip()
        recipes_format = {recipes_name: []}
        ingredients_count = recipes_fl.readline()
        for i in range(int(ingredients_count)):
            ingredient = recipes_fl.readline()
            ingredient_name, quantity, measure = ingredient.strip().split(' | ')
            recipes_format[recipes_name].append({'ingredient_name': ingredient_name,
                                                 'quantity': quantity, 'measure': measure})
        blank_line = recipes_fl.readline()
        cook_book.update(recipes_format)

def get_shop_list_by_dishes(dishes, person_count):
    necessary_ingredients = {}
    for dishe in dishes:
        if dishe in cook_book.keys():
            for ingredient in cook_book[dishe]:
                new_ingredient = dict(ingredient)
                l = new_ingredient['quantity']
                new_in = int(l) * person_count
                new_ingredient['quantity'] = new_in
                if new_ingredient['ingredient_name'] not in necessary_ingredients:
                    necessary_ingredients[new_ingredient['ingredient_name']] = \
                        dict({'measure': new_ingredient['measure'], 'quantity': new_ingredient['quantity']})
                else:
                    necessary_ingredients[new_ingredient['ingredient_name']]['quantity'] += new_ingredient['quantity']
        else:
            return 'Ошибка, нет такого резцепта'
    return necessary_ingredients

def merging_files():
    lin_1 = {}
    for file_name in os.listdir('sorted'):
        with open(os.path.join('sorted', file_name), encoding='utf-8') as f:
            text = f.readlines()
            len_quantity = len(text)
            lin_1[file_name] = len_quantity, text

    lin_2 = {}
    for x in sorted(lin_1, key=lin_1.get):
        lin_2[x] = lin_1[x]

    for key, value in lin_2.items():
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.writelines(f'{key}\n{value[0]}\n{"".join(value[1])}\n')


# print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4))
# merging_files()

