
rules = {}
updates = []

with open("5.txt") as f:
    for line in f:
        if "|" in line:
            a, b = line.strip().split("|")
            if a not in rules:
                rules[a] = []
            rules[a].append(b)
        else:
            if line.strip():
                    updates.append(line.strip().split(","))


def check_order(update: list, fix=False) -> int:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            rule = rules.get(update[j], [])
            if update[i] in rule:
                if fix:
                    update[i], update[j] = update[j], update[i]
                    return check_order(update, True)
                else:
                    return 0
                
    return int(update[len(update) // 2])

result = 0
result2 = 0

for update in updates:
    result += check_order(update)
    result2 += check_order(update, True)

print(result)
print(result2 - result)