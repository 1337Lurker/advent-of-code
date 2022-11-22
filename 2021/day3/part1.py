import fileinput


def main():
    diagnostic_numbers = [bit_string.strip() for bit_string in fileinput.input()]

    gamma_rate_string = ""
    epsilon_rate_string = ""

    for position in range(len(diagnostic_numbers[0])):
        zero, one = 0, 0

        for diagnostic_number in diagnostic_numbers:
            number = diagnostic_number[position]
            if number == "0":
                zero += 1
            elif number == "1":
                one += 1
            else:
                raise Exception

        most_common = b""
        least_common = b""
        print(f"position: {position}")
        print(f"zero: {zero}")
        print(f"one: {one}")
        if zero > one:
            most_common = "0"
            least_common = "1"
        else:
            most_common = "1"
            least_common = "0"

        gamma_rate_string += most_common
        epsilon_rate_string += least_common

    gamma_rate = int(gamma_rate_string, 2)
    epsilon_rate = int(epsilon_rate_string, 2)
    power_consumption = gamma_rate * epsilon_rate
    print(f"gamma rate: {gamma_rate}")
    print(f"epsilon rate: {epsilon_rate}")
    print(f"power_consumption: {power_consumption}")


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
