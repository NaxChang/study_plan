import csv

filedname = ["姓名", "身高", "體重"]
with open("test03.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, filedname)
    writer.writeheader()
    writer.writerow({"姓名": "Nameless", "身高": 173, "體重": 76})
    writer.writerow({"姓名": "Joanna", "身高": 164, "體重": 76})
# "姓名", "身高", "體重"
# "姓名": "Nameless", "身高": 173, "體重": 76
# "姓名": "Joanna", "身高": 164, "體重": 76
