triplet_to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

digit_to_triplet = {v: k for k, v in triplet_to_digit.items()}

s = input()

# находим операцию
for op in "+-*":
    if op in s:
        operator = op
        parts = s.split(op)
        break

# функция, чтобы превратить triplet-строку в число
def triplet_to_number(triplet_str):
    digits = [triplet_to_digit[triplet_str[i:i+3]] for i in range(0, len(triplet_str), 3)]
    return int("".join(digits))

num1 = triplet_to_number(parts[0])
num2 = triplet_to_number(parts[1])

# вычисляем результат
if operator == '+':
    res = num1 + num2
elif operator == '-':
    res = num1 - num2
else:
    res = num1 * num2

# переводим результат обратно в triplet
res_str = "".join(digit_to_triplet[d] for d in str(res))
print(res_str)
