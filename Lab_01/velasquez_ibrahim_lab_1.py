 #!/usr/bin/env python3
"""Module docstring."""
from csv import DictReader
from typing import TextIO
from pathlib import Path
import pprint

def open_file() -> TextIO:
    """IT opens a csv file and reads it using the csv module

        returns:
            a dict containing indian_food
    """
    while True:
        try:
            # user_file = "indian_food_small.csv"
            user_file = input("Input a file name: ")
            THIS_FOLDER = Path(__file__).parent.resolve()
            user_file = THIS_FOLDER / user_file
            with open(user_file, "r", encoding="utf8") as indian_food:
                data = build_dictionary(indian_food)
                break
        except FileNotFoundError as e:
            print(f"{e}, please try again.")
    return data
def build_dictionary(file: TextIO) -> dict[str, dict[str, dict[str, list]]]:
    """Insert Docstring"""
    csv_reader = DictReader(file)
    data = {}
    for row in csv_reader:
        name = row["name"].lower()
        ingredients = set(row["ingredients"].split(","))
        diet = row["diet"]
        prep_time = row["prep_time"]
        cook_time = row["cook_time"]
        flavor_profile = row["flavor_profile"]
        course = row["course"]
        state = row["state"]
        region = row["region"]

        if region not in data:
            data[region] = {}
        if state not in data[region]:
            data[region][state] ={}
        if name not in data[region][state]:
            data[region][state][name] = {
                "ingredients" : ingredients, 
                "diet" : diet, 
                "prep_time" : prep_time, 
                "cook_time" : cook_time, 
                "flavor_profile" : flavor_profile, 
            }

    return data   

def get_ingredients(data: dict, foods: list[str]) -> set[str]:
    """Takes main dictionary and a list of foods provided by the user and returns a set of ingredients
    needed for those foods.
        args:
            data: dict containing csv file for indian_foods.
            foods: list of foods given by the user.
        returns:
            set: of all ingredients for those foods.
    """
    ingredients_set = set()
    items = list(data.values())
    for region in items:
        state = list(region.values())
        for name in state:
             for names in foods:
                if names in name:
                    user_foods = name[names]
                    for ingredient in user_foods["ingredients"]:
                        ingredients_set.add(ingredient.lower().strip())
    
    return ingredients_set
        


# indian_food_small.csv

def get_useful_and_missing_ingredients(
    data: dict, foods: list[str], pantry: list[str]
) -> tuple[list[str], list[str]]:
    """Takes main dictionary, list of foods by user, and ingredients by the user and
    returns a tuple containing the useful ingredients and the missing ingredients for the foods specified by the user.
        Args:
            data: dict containing csv file for indian_foods.
            pantry: list of ingredients given by the user.
            foods: list of foods given by the user.
        returns:
            tuple: containing useful and needed ingredients for the foods.
    """
    dishes = get_ingredients(data, foods)
    pantry = set(pantry)
    ingredients_you_have_and_need = dishes & pantry
    ingredients_to_purchase = dishes - pantry
    tuple1 = sorted(ingredients_you_have_and_need), sorted(ingredients_to_purchase)
    return tuple1





def get_list_of_foods(data: dict, ingredients: list[str]) -> list[str]:
    """Takes the main dictionary and a list of ingredients and gives back a list of foods that
        can be made with those ingredients.
        Args:
            data: dict containing csv file for indian_foods
            ingredients: list of ingredients given by the user.
        returns:
            a list of foods.
    """
    food_list = []
    ingredients = set(ingredients)
    for region, state in data.items():
        for state, food_name in state.items():
            for food_name, ingredient in food_name.items():
                ingredients_set = ingredient["ingredients"]
                ingredients_set = set(map(str.strip, ingredients_set))
                ingredients_set = set(map(str.lower, ingredients_set))
                if ingredients_set.issubset(ingredients):
                    food_list.append(food_name)
    
    return food_list


def get_food_by_preference(data: dict, preferences: list[str]) -> list[str]:
    """
    """
    pass  # replace this line with your code


def main():
    print("Indian Foods & Ingredients.\n")
    MENU = """
        A. Input various foods and get the ingredients needed to make them!
        B. Input various ingredients and get all the foods you can make with them!
        C. Input various foods and ingredients and get the useful and missing ingredients!
        D. Input various foods and preferences and get only the foods specified by your preference!
        Q. Quit
            """
    file = open_file()
    user_input = ""
    while user_input != "q":
        print(MENU)
        user_input = input("Your choice: ").lower()
        choice_list = "a", "b", "c", "d", "e", "q"
        list(choice_list)
        if user_input not in choice_list:
            print("invalid input. Please enter a valid input (A_D, Q)")
        elif user_input == "a":
            foods_user = input("Enter foods, separated by commas: ").lower()
            foods_user = foods_user.split(",")
            foods_user = (list(map(str.strip, foods_user)))
            print(get_ingredients(file, foods_user))
        elif user_input == "b":
            ingredients_user = input("Enter ingredients, separated by commas: ").lower()
            ingredients_user = ingredients_user.split(",")
            ingredients_user = (list(map(str.strip, ingredients_user)))
            print("Foods:")
            print(get_list_of_foods(file, ingredients_user))
        elif user_input == "c":
            foods_user = input("Enter foods, separated by commas: ").lower()
            foods_user = foods_user.split(",")
            foods_user = (list(map(str.strip, foods_user)))
            ingredients_user = input("Enter ingredients, separated by commas: ").lower()
            ingredients_user = ingredients_user.split(",")
            ingredients_user = (list(map(str.strip, ingredients_user)))
            tuple2 = get_useful_and_missing_ingredients(file, foods_user, ingredients_user)
            print(f"Useful Ingredients: {tuple2[0]}")
            print(f"Missing ingredients: {tuple2[1]}")
        elif user_input == "d":
            print("coming on the next update!")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()