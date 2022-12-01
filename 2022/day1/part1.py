import fileinput

def main():
    elves = [[]]
    with fileinput.input() as calories:
        for calorie in calories:
            if calorie == "\n":
                elves.append([])
            else:
                elves[-1].append(int(calorie))
    elves_calories = [sum(elf) for elf in elves]

    elves_calories.sort()
    elves_calories.reverse()
    print(elves_calories[0] + elves_calories[1] +elves_calories[2])

    return

if __name__=="__main__":
    print(main())

