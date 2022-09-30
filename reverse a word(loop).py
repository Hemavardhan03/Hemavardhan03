string=input("enter the string:")
reverse_string=""
index=len(string)
while index>0:
    reverse_string+=string[index-1]
    index=index-1
    print(reverse_string)