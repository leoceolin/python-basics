#  read file
# with open("datasets/student.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# read file line by line
with open("datasets/student.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Hello, {line.rstrip()}")
