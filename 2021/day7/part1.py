import fileinput


def main():
    crab_input = [line.split(",") for line in fileinput.input()]

    crab_positions = [int(crab_position) for crab_position in crab_input[0]]

    min_position = min(crab_positions)
    max_position = max(crab_positions)
    ideal_position = -1
    ideal_position_fuel_spent = 0

    for i in range(min_position, max_position + 1):

        fuel_spent = 0
        for crab in crab_positions:
            fuel_spent += abs(i - crab)
        # print(f"fuel spent to align at {i}: {fuel_spent}")

        if ideal_position < 0:
            ideal_position = i
            ideal_position_fuel_spent = fuel_spent
            print(f"ideal alignment: {ideal_position}")
            print(f"ideal fuel spent: {ideal_position_fuel_spent}")
        elif fuel_spent < ideal_position_fuel_spent:
            ideal_position = i
            ideal_position_fuel_spent = fuel_spent
            print(f"ideal alignment: {ideal_position}")
            print(f"ideal fuel spent: {ideal_position_fuel_spent}")

    return ideal_position


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
