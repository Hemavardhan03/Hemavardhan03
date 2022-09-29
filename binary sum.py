def getbinary(num):
    if num>=1:
        getbinary(num//2)
        print(num%2,end="")
a=int(input("enter the number"))
b=int(input("enter the num"))
