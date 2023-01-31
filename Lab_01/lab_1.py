#!/usr/bin/env python3
"""Module docstring."""
from csv import DictReader
from typing import TextIO


def open_file() -> TextIO:
    """Insert Docstring"""
    with open("indian_food.csv", "r", encoding="utf8") as indian_food:
        csv_reader = DictReader(indian_food)
        print(csv_reader[0])

    return 

def build_dictionary(file: TextIO) -> dict[str, dict[str, dict[str, list]]]:
    """Insert Docstring"""
    for row in file:
        data = data.append(row)
        print(data)


def get_ingredients(data: dict, foods: list[str]) -> set[str]:
    """Insert Docstring"""
    pass  # replace this line with your code


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
    print(open_file())
    
