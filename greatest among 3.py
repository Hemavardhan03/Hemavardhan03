print("enter three integers")
a = int(input())
b = int(input())
c = int(input())
if(a>b and a>c):
    print("%d is greatest" %(a))
elif(b>c):
    print("%d is greatest" %(b))
else:
    print("%d is greatest" %(c))

