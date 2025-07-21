file_path = "example.txt"
with open(file_path, "r+") as file:
    file.write("kyo")
    content = file.read()
    print(content)
# file = open(file_path, "r")


# file.close()
