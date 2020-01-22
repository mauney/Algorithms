#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # initialize number of batches to a really large number
    num_batches = float("inf")
    # for each ingredient in recipe
    for ingredient, amount in recipe.items():
        # reduce the number of batches if necessary
        num_batches = min(num_batches, ingredients.get(ingredient, 0) // amount)
        # if number of batches is zero, we can stop calculating
        if num_batches == 0:
            break
  
    return num_batches 


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))