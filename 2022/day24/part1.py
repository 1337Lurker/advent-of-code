import fileinput

def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]

    return


if __name__ == "__main__":
    print(main())
