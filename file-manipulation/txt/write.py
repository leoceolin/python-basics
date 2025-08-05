name = input("Enter the student name: \n")

""""
Files - open, read, write, close
1-> Mode W - Write
2-> Mode A - Append
3-> Mode R - Read
"""

# First implementation with open and close
# file = open("datasets/student.txt", "a", encoding="utf-8")
# file.write(f"Name: {name}\n")
# file.close()


# Second implementation using with and open
with open("datasets/student.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}\n")

print("Student information has been written to /datasets/student.txt")
