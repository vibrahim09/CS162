#!/usr/bin/env python3
"""Module docstring."""
from csv import DictReader
from typing import TextIO
from pathlib import Path
import pprint

def open_file() -> TextIO:
    """Insert Docstring"""
    while True:
        try:
            user_file = "indian_food_small.csv"
            # user_file = input("Input a file name: ")
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
        name = row["name"]
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
    """Insert Docstring"""
    items = list(data.values())
    for region in items:
        state = list(region.values())
        for name in state:
             for names in foods:
                if names in name:
                    user_foods = name[names]
                    print(user_foods["ingredients"])
        


# indian_food_small.csv

def get_useful_and_missing_ingredients(
    data: dict, foods: list[str], pantry: list[str]
) -> tuple[list[str], list[str]]:
    """Insert Docstring"""
    get_ingredients(data, foods)




def get_list_of_foods(data: dict, ingredients: list[str]) -> list[str]:
    """Insert Docstring"""
    pass  # replace this line with your code


def get_food_by_preference(data: dict, preferences: list[str]) -> list[str]:
    """Insert Docstring"""
    pass  # replace this line with your code


def main():
    print("Indian Foods & Ingredients.\n")
    MENU = """
        A. Input various foods and get the ingredients needed to make them!
        B. Input various ingredients and get all the foods you can make with them!
        C. Input various foods and ingredients and get the useful and missing ingredients!
        D. Input various foods and preferences and get only the foods specified by your preference!
        Q. Quit
        : """

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
    file = open_file()
    print(file)
    print("\n")
    get_ingredients(file, ["Balu shahi", "Ghevar"])
    ingredients_you_have = ["milk", "sugar", "ghee", "rice", "nuts"]
    get_useful_and_missing_ingredients(file, ["Balu shahi", "Ghevar"], ingredients_you_have)
