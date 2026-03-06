import re

s = input().strip()

m = re.match(r"Name:\s*(.+),\s*Age:\s*(\d+)", s)
if m:
    print(m.group(1), m.group(2))