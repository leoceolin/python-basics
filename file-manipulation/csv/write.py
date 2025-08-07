import csv

language = input("Enter a language: ")
category = input("Enter a category: ")

with open("datasets/data.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([language, category])
