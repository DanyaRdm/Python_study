# ферзь
x1 = int(input())  # 1
y1 = int(input())  # 1
x2 = int(input())  # 2
y2 = int(input())  # 2
if x1 == x2 or y1 == y2:
    print("YES")
elif (x1 - x2 == y1 - y2) or (x1 - x2 == y2 - y1) or (x2 - x1 == y1 - y2) or (x2 - x1 == y2 - y1):
    print("YES")
else:
    print("NO")
