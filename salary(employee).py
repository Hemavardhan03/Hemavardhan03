grade =input("enter the grade of the employee=")
salary = int(input("enter the salary of employee="))

bonus5 = salary+(salary*0.05)
bonus10 = salary+(salary*0.1)
bonus12 = salary+(salary*0.12)
bonus7 = salary+(salary*0.07)
if grade=="A" or grade=="B":
    if salary < 10000 and grade == "A":
     print("salary=",salary)
     print("bonus=",salary*0.07)
     print("total to be paid=", bonus7)
    elif salary < 10000 and grade == "B":
     print("salary=", salary)
     print("bonus=", salary * 0.12)
     print("total to be paid=", bonus12)
    elif salary >= 10000 and grade == "B":
     print("salary=", salary)
     print("bonus=", salary * 0.1)
     print("total to be paid=", bonus10)
    elif salary >= 10000 and grade == "A":
     print("salary=",salary)
     print("bonus=", salary * 0.05)
     print("total to be paid=", bonus5)
    else:
        print("please enter valid input")


