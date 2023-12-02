import os
import re

os.chdir(os.path.dirname(os.path.realpath(__file__)))

digit_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}

#Take in text numbers as well
def extract_digits(input):
    input = input.lower().strip()
    digits = []
    for i in range(len(input)):
        if input[i] in digit_mapping.values():
            digits.append(input[i])
        else:
            for key, value in digit_mapping.items():
                substring = input[i:i+len(key)]
                if substring == key:
                    digits.append(value)
    return digits

#only take numeric digits
def extract_digits_numeric(input):
    input = input.lower().strip()
    digits = []
    for i in range(len(input)):
        if input[i] in digit_mapping.values():
            digits.append(input[i])
    return digits

with open("input.txt") as f:
    total = 0
    for line in f.readlines():
        print(line)
        digits = extract_digits(line)
        print(digits)
        if len(digits) == 0:
            pass
        elif len(digits) == 1:
            print("CALLIBRATION: " + str(digits[0]) + str(digits[0]))
            total += int(str(digits[0]) + str(digits[0]))
        else:
            print("CALLIBRATION: " + str(digits[0]) + str(digits[-1]))
            total += int(str(digits[0]) + str(digits[-1]))
print(total)
        

        