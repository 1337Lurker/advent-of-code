import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    raw_rules = []
    raw_pages = []
    for line in raw_input:
        if "|" in line:
            raw_rules.append(line)
        elif "," in line:
            raw_pages.append(line)

    rules = []
    for rule in raw_rules:
        rules.append(Rule(*rule.split("|")))

    pages = []
    for page in raw_pages:
        pages.append(Page(page.split(",")))

    valid_pages = []
    for index, page in enumerate(pages,1):
        if page.is_valid(rules):
            valid_pages.append(page)
            print(f"Page #{index} is valid.")
        else:
            print(f"Page #{index} is not valid.")

    middle_pages = []
    for page in valid_pages:
        middle_pages.append( page.middle_page())

    return sum(middle_pages)


class Rule:
    def __init__(self, leading_page: str, trailing_page: str):
        self.leading_page = leading_page
        self.trailing_page = trailing_page


class Page:
    def __init__(self, pages: list[str]):
        self.pages = pages

    def middle_page(self) -> str:
        page_count = len(self.pages)
        middle = int(page_count / 2)
        return int(self.pages[middle])

    def is_valid(self, rules: list[Rule]) -> bool:
        for rule in rules:
            if (
                rule.leading_page in self.pages
                and rule.trailing_page in self.pages
                and self.pages.index(rule.leading_page)
                > self.pages.index(rule.trailing_page)
            ):
                return False

        return True


if __name__ == "__main__":
    print(main())
