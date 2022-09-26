import cmath
print("enter a,b,c1")
a = int(input())
b = int(input())
c = int(input())

d = (b**2)-(4*a*c)
ans1 = (-b-cmath.sqrt(d))/(2*a)
ans2 = (-b+cmath.sqrt(d))/(2*a)
print("the roots are")
print(ans1)
print(ans2)


