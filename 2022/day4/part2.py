import fileinput
import string


class Assignment:
    @staticmethod
    def parse(assignment: str):
        assignment_start, _separator, assignment_stop = assignment.partition("-")
        return set(range(int(assignment_start), int(assignment_stop) + 1))


def main():
    overlapped_assignments = 0
    with fileinput.input() as assignments:
        for assignment in assignments:
            assignment_pair = assignment.strip().split(",")

            first = Assignment.parse(assignment_pair[0])
            second = Assignment.parse(assignment_pair[1])

            if not first.isdisjoint(second):
                overlapped_assignments += 1

    return overlapped_assignments


if __name__ == "__main__":
    print(main())
