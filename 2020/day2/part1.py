import fileinput
import math
import re


def main():
    print("hello world")
    passwords_with_reqs = [password_req for password_req in fileinput.input()]
    valid_passwords = []

    for i, password_with_req in enumerate(passwords_with_reqs):
      requirements, password = password_with_req.split(':')
      password = password.strip()
      min_count = int(requirements.split('-')[0])
      max_count = int(requirements.split(' ')[0].split('-')[1])
      required_letter = requirements.split(' ')[1]
      pattern = f"({required_letter}){{{min_count},{max_count}}}"

      letter_count=0
      for letter in list(password):
        if letter == required_letter:
          letter_count += 1

      if letter_count >= min_count and letter_count <= max_count:
        valid_passwords.append(password_with_req)
      
    return len(valid_passwords)

if __name__ == "__main__":
    # execute only if run as a script
    print(main())
