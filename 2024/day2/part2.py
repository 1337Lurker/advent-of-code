import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    safe_levels = 0
    for report in raw_input:
        levels = report.split()
        levels = [int(level) for level in levels]
        if is_safe(report=levels):
            safe_levels += 1
            print(f"Level '{levels}' is Safe")
        else:
            print(f"Level '{levels}' is Unsafe")
        continue

    print(f"There are {safe_levels} safe reports.")


def is_safe(report: list):
    ascends = levels_ascend(report=report)
    descends = levels_descend(report=report)
    if ascends or descends:
        return True
    return False


def levels_ascend(report: list, damper_used: bool = False) -> bool:
    for index in range(len(report)):
        previous_index = index - 1
        next_index = index + 1
        if (
            previous_index >= 0
            and (
                report[index] <= report[previous_index]
                or (report[index] - report[previous_index]) > 3
            )
        ) or (
            next_index < len(report)
            and (
                report[next_index] <= report[index]
                or (report[next_index] - report[index]) > 3
            )
        ):
            if damper_used:
                return False

            previous_removed_safe = False
            if previous_index >= 0:
                report_remove_previous = report.copy()
                report_remove_previous.pop(previous_index)
                previous_removed_safe = levels_ascend(
                    report=report_remove_previous, damper_used=True
                )
            report_remove_current = report.copy()
            report_remove_current.pop(index)
            current_removed_safe = levels_ascend(
                report=report_remove_current, damper_used=True
            )

            next_removed_safe = False
            if next_index < len(report):
                report_remove_next = report.copy()
                report_remove_next.pop(next_index)
                next_removed_safe = levels_ascend(
                    report=report_remove_next, damper_used=True
                )
            if previous_removed_safe:
                print(f"{report} was unsafe. {report_remove_previous} made it safe.")
            if current_removed_safe:
                print(f"{report} was unsafe. {report_remove_current} made it safe.")
            if next_removed_safe:
                print(f"{report} was unsafe. {report_remove_next} made it safe.")
            return previous_removed_safe or current_removed_safe or next_removed_safe
    return True


def levels_descend(report: list) -> bool:
    reversed_report = report.copy()
    reversed_report.reverse()
    reversed_level_ascends = levels_ascend(reversed_report)
    return reversed_level_ascends


if __name__ == "__main__":
    print(main())
