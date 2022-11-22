import fileinput


def most_least_common_bit(bit_strings, position, tie_breaker_bit="1"):
    zero, one = 0, 0
    for bit_string in bit_strings:
        bit = bit_string[position]
        if bit == "0":
            zero += 1
        elif bit == "1":
            one += 1
        else:
            raise Exception

    most_common = b""
    least_common = b""
    print(f"zero: {zero}")
    print(f"one: {one}")
    if zero > one:
        most_common = "0"
        least_common = "1"
    elif one > zero:
        most_common = "1"
        least_common = "0"
    else:
        return ("1", "0")

    return (most_common, least_common)


def bit_rating_filter(
    bit_strings,
    bit_filter,
    bit_position=0,
    prefer_most_common=True,
    tie_breaker_bit="1",
):
    filtered_bit_strings = []
    for bit_string in bit_strings:
        if bit_string[bit_position] == bit_filter:
            filtered_bit_strings.append(bit_string)

    if len(filtered_bit_strings) == 1:
        return filtered_bit_strings[0]

    most_common, least_common = most_least_common_bit(
        filtered_bit_strings, bit_position + 1, tie_breaker_bit
    )
    print(f"position: {bit_position}")
    print(f"most_common: {most_common}")
    print(f"least_common: {least_common}")
    print(f"filtered_strings: {filtered_bit_strings}")

    if prefer_most_common:
        return bit_rating_filter(
            filtered_bit_strings,
            most_common,
            bit_position + 1,
            prefer_most_common,
            tie_breaker_bit,
        )

    return bit_rating_filter(
        filtered_bit_strings,
        least_common,
        bit_position + 1,
        prefer_most_common,
        tie_breaker_bit,
    )


def main():
    diagnostic_numbers = [bit_string.strip() for bit_string in fileinput.input()]

    o2_generator_first_bit = ""
    co2_scrubber_first_bit = ""

    most_common, least_common = most_least_common_bit(diagnostic_numbers, 0)
    o2_generator_first_bit = most_common
    co2_scrubber_first_bit = least_common

    o2_generator_diagnostics = bit_rating_filter(
        diagnostic_numbers, o2_generator_first_bit, 0, True, "1"
    )
    co2_scrubber_diagnostics = bit_rating_filter(
        diagnostic_numbers, co2_scrubber_first_bit, 0, False, "0"
    )

    o2_generator_rating = int(o2_generator_diagnostics, 2)
    co2_scrubber_rating = int(co2_scrubber_diagnostics, 2)
    life_support_rating = o2_generator_rating * co2_scrubber_rating
    print(f"o2 generator rating: {o2_generator_rating}")
    print(f"co2 scrubber rating: {co2_scrubber_rating}")
    print(f"life support rating: {life_support_rating}")


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
