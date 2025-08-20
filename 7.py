a = int(input())
b = int(input())
c = int(input())
if a == 90 or b == 90 or c == 90:
    print("Right triangle")
elif a+b+c==180:
    print("Obtuse triangle")
else:
    print("Acute triangle")
