import fileinput
import math


def main():
    fuel_required = 0

    for mass in fileinput.input():
        fuel_required += calculate_fuel_for(mass)
    print(fuel_required)


def calculate_fuel_for(mass):
    fuel_required = math.floor(int(mass) / 3) - 2
    if fuel_required > 0:
        return fuel_required + calculate_fuel_for(fuel_required)
    else:
        return 0


if __name__ == "__main__":
    # execute only if run as a script
    main()

