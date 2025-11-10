a = int(input())
b = int(input())
c = int(input())
if a > b > c:
    print(a, b, c, sep='\n')
elif a > c > b:
    print(a, c, b, sep='\n')
elif b > a > c:
    print(b, a, c, sep='\n')
elif b > c > a:
    print(b, c, a, sep='\n')
elif c > a > b:
    print(c, a, b, sep='\n')
elif c > b > a:
    print(c, b, a, sep='\n')



