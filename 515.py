import re

s = input()

def double_digit(match):
    return match.group() * 2  # repeat the matched digit

result = re.sub(r"\d", double_digit, s)
print(result)