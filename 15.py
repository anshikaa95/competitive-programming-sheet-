per = float(input("Enter percentage: "))
if per < 25:
    print("D")
elif per <= 45:
    print("C")
elif per <= 65:
    print("B")
elif per <= 85:
    print("A")
else:
    print("A+")
