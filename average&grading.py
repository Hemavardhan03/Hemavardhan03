print("enter marks=")
m1 = int(input())
m2 = int(input())
m3 = int(input())
m4 = int(input())
m5 = int(input())
total = m1+m2+m3+m4+m5
average = total/5
print("average = %d" %(average))
if average>=90:
    print("grade is A")
elif average>=70 and average<90:
    print("grade is B")
elif average>=40 and average<70:
    print("grade is C")
else:
    print("fail")

