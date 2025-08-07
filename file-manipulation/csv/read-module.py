import csv

courses = []

with open("datasets/data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        courses.append(
            {
                "language": row["language"],
                "category": row["category"],
            }
        )
print(courses)
