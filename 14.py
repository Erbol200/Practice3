# ввод массива
n = int(input())
arr = list(map(int, input().split()))

# ввод операций
q = int(input())
operations = [input().split() for _ in range(q)]

# применяем операции по порядку
for op in operations:
    if op[0] == "add":
        x = int(op[1])
        arr = list(map(lambda a: a + x, arr))
    elif op[0] == "multiply":
        x = int(op[1])
        arr = list(map(lambda a: a * x, arr))
    elif op[0] == "power":
        x = int(op[1])
        arr = list(map(lambda a: a ** x, arr))
    elif op[0] == "abs":
        arr = list(map(lambda a: abs(a), arr))

# вывод
print(*arr)
