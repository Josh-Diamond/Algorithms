#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    total_batches_per_ingredient = []
    if set(ingredients) >= set(recipe):
        for item in recipe:
            if recipe[item] > ingredients[item]:
                total_batches_per_ingredient.append(0)
            else:
                total_batches_per_ingredient.append((ingredients[item] // recipe[item]))
        return min(total_batches_per_ingredient)
    else:
        return 0

# Test Cases
# rec_1 = {'milk': 100, 'flour': 4, 'sugar': 10}
# ing_1 = {'milk': 1288, 'flour': 9, 'sugar': 95}
# rec_2 = {'milk': 100, 'flour': 4, 'sugar': 10}
# ing_2 = {'milk': 1288, 'flour': 12, 'sugar': 95}
# rec_3 = {'milk': 100, 'flour': 4, 'sugar': 10}
# ing_3 = {'milk': 1, 'flour': 12, 'sugar': 95}
# 
# print(recipe_batches(rec_1, ing_1))
# print(recipe_batches(rec_2, ing_2))
# print(recipe_batches(rec_3, ing_3))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))