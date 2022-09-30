t_users=int(input("enter total users="))
staff_users=int(input("enter staff users="))
non_t_users=staff_users/3
if t_users>0 and staff_users>0:
    stud_users = t_users-staff_users-non_t_users
    print("student users=",stud_users)
else:
    print("invalid input")
