names = []
with open("datasets/student.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip())


for name in sorted(names):
    print(f"Hello, {name}")
