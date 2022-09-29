n=int(input("enter number of words"))
words=[]
print("enter the words")
for i in range(0,n):
    y=str(input())
    words.append(y)

print("words=",words)
words.sort()
print("the ascending sorted list are",words)

words.sort(reverse=True)
print("the descending sorted list are=",words)