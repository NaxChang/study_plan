import csv

with open("test01.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["姓名", "身高", "體重"])
    writer.writerow(["Nameless", "173", "76"])
    writer.writerow(["Joanna", "164", "76"])
"""
"姓名", "身高", "體重"
"Nameless", "173", "76"
"Joanna", "164", "76"
"""
