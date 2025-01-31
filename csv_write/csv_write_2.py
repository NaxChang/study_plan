import csv

csv_table = [
    ["姓名", "身高", "體重"],
    ["Nameless", "173", "76"],
    ["Joanna", "164", "76"],
]

with open("test02.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_table)

# "姓名", "身高", "體重"
# "Nameless", "173", "76"
# "Joanna", "164", "76"
