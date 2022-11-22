import fileinput


def main():

    input = [line for line in fileinput.input()]
    output = 0
    for input in input:
        wire_inputs, display_outputs = input.split("|")
        wire_inputs = wire_inputs.split()
        display_outputs = display_outputs.split()

        one = None  # 2 char
        seven = None  # 3 char
        four = None  # 4 char
        eight = None  # 7 char

        for input in wire_inputs:
            if len(input) == 2:
                one = set(input)
            elif len(input) == 3:
                seven = set(input)
            elif len(input) == 4:
                four = set(input)
            elif len(input) == 7:
                eight = set(input)

        two = None  # 5 char
        three = None  # 5 char
        five = None  # 5 char

        six = None  # 6 char
        nine = None  # 6 char
        zero = None  # 6 char

        a = seven - one
        bd = four - one
        cf = one
        eg = eight - seven - four

        for input in wire_inputs:
            if len(input) == 6 and set(input) > seven | four:
                nine = set(input)
        g = nine - seven - four
        e = eg - g

        for input in wire_inputs:
            if len(input) == 6 and set(input) > seven | eg:
                zero = set(input)
        b = zero - seven - eg
        d = bd - b

        for input in wire_inputs:
            if len(input) == 5 and set(input) > a | d | eg:
                two = set(input)
        c = two - a - d - eg
        f = cf - c
        three = a | c | d | f | g
        five = eight - c - e
        six = eight - c

        output_string = ""
        for display_output in [set(display_digit) for display_digit in display_outputs]:
            if display_output == one:
                output_string += '1'
            elif display_output == two:
                output_string += "2"
            elif display_output == three:
                output_string += "3"
            elif display_output == four:
                output_string += "4"
            elif display_output == five:
                output_string += "5"
            elif display_output == six:
                output_string += "6"
            elif display_output == seven:
                output_string += "7"
            elif display_output == eight:
                output_string += "8"
            elif display_output == nine:
                output_string += "9"
            elif display_output == zero:
                output_string += "0"
            else:
                raise Exception("NUMBER NOT FOUND")
        output += int(output_string)

    return output


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
