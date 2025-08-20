a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    print(a,"is the minimum value among three")
elif b <= a and b <= c:
    print(b,"is the minimum value among three")
else:
    print(c,"is the minimum value among three")
