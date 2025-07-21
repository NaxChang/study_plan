for i in range(10):
    if i == 2 or i == 5 or i == 8:
        continue
    if i == 7:
        break

    print(i)
print("Out of loop")
