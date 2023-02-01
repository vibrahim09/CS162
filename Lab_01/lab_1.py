#!/usr/bin/env python3
"""Module docstring."""
from csv import DictReader
from typing import TextIO


def open_file() -> TextIO:
    """Insert Docstring"""
    while True:
        try:
            user_file = input("Input a file name: ")
            with open(user_file, "r", encoding="utf8") as indian_food:
                build_dictionary(indian_food)
                break
        except FileNotFoundError as e:
            print(f"{e}, please try again.")

def build_dictionary(file: TextIO) -> dict[str, dict[str, dict[str, list]]]:
    """Insert Docstring"""
    csv_reader = DictReader(file)
    data = {}
    for row in csv_reader:
        name = row["name"]
        ingredients = row["ingredients"]
        diet = row["diet"]
        prep_time = row["prep_time"]
        cook_time = row["cook_time"]
        flavor_profile = row["flavor_profile"]
        course = row["course"]
        state = row["state"]
        region = row["region"]

        if region not in data:
            data[region] = {}
        if state not in data:
            data[region][state] ={}
        if name not in data:
            data[region][state] ={name}

        data[region][state] = {name : [ingredients, diet, (prep_time, cook_time), flavor_profile]} 
            
    print(data)

def get_ingredients(data: dict, foods: list[str]) -> set[str]:
    """Insert Docstring"""
    pass  # replace this line with your code
# indian_food_small.csv

def get_useful_and_missing_ingredients(
    data: dict, foods: list[str], pantry: list[str]
) -> tuple[list[str], list[str]]:
    """Insert Docstring"""
    pass  # replace this line with your code


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
