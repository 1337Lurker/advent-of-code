def main():
    valid_numbers = []
    for number in range(271973, 785962):
        if adjacent_digits(number) and has_only_increasing_digits(number):
            valid_numbers.append(number)
    print(len(valid_numbers))


def adjacent_digits(number):
    number = str(number)
    preceding_digit = "X"
    adjacent_count = 1
    for index in range(0, 6):
        if number[index] == preceding_digit:
            adjacent_count += 1
        else:
            if adjacent_count == 2:
                return True
            preceding_digit = number[index]
            adjacent_count = 1

    if adjacent_count == 2:
        return True

    return False


def has_only_increasing_digits(number):
    number = str(number)
    for i in range(0, 5):
        if number[i] > number[i + 1]:
            return False
    return True


if __name__ == "__main__":
    # execute only if run as a script
    main()
