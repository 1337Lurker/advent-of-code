import fileinput


def main():

    input = [line for line in fileinput.input()]
    unique_segment_number_outputs = 0
    for line in input:
        wire_inputs, display_outputs = line.split("|")
        wire_inputs = wire_inputs.split()
        display_outputs = display_outputs.split()

        for display_output in display_outputs:
            segment_count = len(display_output)
            if segment_count in [2,3,4,7]:
                unique_segment_number_outputs += 1

    return unique_segment_number_outputs


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
