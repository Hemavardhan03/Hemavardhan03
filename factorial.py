print("enter number rto find factorial=")
n = int(input())
factorial = 1
if n<0:
    print("factorial does not exist for negative")
elif n==0:
    print("factorial=1")
else:
    for i in range(1, n+1):
      factorial = factorial*i
    print("factorial=%d" % (factorial))

