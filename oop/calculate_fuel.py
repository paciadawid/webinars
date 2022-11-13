from math import floor


def calculate_fuel(mass):
    fuel = floor(mass / 3) - 2
    fuel = int(mass/3) - 2
    fuel = mass // 3 - 2
    return fuel
