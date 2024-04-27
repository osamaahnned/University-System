Student_Data = []
Admin_Data = [{"username":"Gebaly","password":"1234"}]
id = 1
#-------------------------------------------------------
def add_student():
    global id
    name=input("enter student name: ")
    while(True):
        try:
            age=int(input("enter student age: "))
            break
        except:
            print("Please enter an integer value!!")

    while True:
        try:
            gpa = float(input("enter current GPA: "))
            break
        except:
            print("please enter a float value!!")

    while True:
        chk_not_joined_if = True
        for i in Student_Data:  # for duplication (check all dicts without find the same id)
            if i["ID"] == id:
                chk_not_joined_if=False
                id+=1
                break
        if(chk_not_joined_if):
            break
    student_id = id

    password = input("Enter Password: ")

    Student_Data.append({"ID":student_id , "Name":name , "Age":age , "GPA":gpa , "username":name+str(student_id), "password":password})
    print(name + " has been added!!")
def edit_student():
    print(Student_Data)
    edit_id = int(input("Enter Current Student ID: "))
    cnt = 0
    chk_no_current_id = True
    for i in Student_Data:
        if i["ID"] == edit_id:
            chk_no_current_id = False
            name = input("enter New student name: ")
            while (True):
                age = int(input("enter New student age: "))
                if type(age) is not int:
                    print("Please enter an integer value!!")
                    continue
                else:
                    break
            while (True):
                gpa = float(input("enter a New GPA: "))
                if type(gpa) is not float:
                    print("please enter a float value!!")
                    continue
                else:
                    break
            while (True):
                chk_id = True
                NEW_ID = int(input("enter New ID: "))
                if type(NEW_ID) is not int:
                    print("please enter a float value!!")
                    continue
                for i in Student_Data: # for duplication
                    if i["ID"] == NEW_ID:
                        print("This ID is already Used!!")
                        chk_id = False
                        break
                if chk_id == True:
                    break
            Student_Data[cnt][{"ID": NEW_ID, "Name": name, "Age": age, "GPA": gpa}]
        else:
            cnt += 1
    if chk_no_current_id:
        print("No Editing <3")
    else:
        print("Done  >_<  <3")

def delete_student():
    print(Student_Data)
    cnt = 0
    chk_no_current_id = True
    delete_id = int(input("Enter Student ID to delete or zero to exit: "))
    for i in Student_Data:
        if i["ID"] == delete_id:
            chk_no_current_id = False
            confirm_delete=input("Press Y to confirm or N to cancel: ")
            if confirm_delete == "Y" or confirm_delete == "y":
                del Student_Data[cnt]
                chk_delete=True
            else:
                chk_delete = False
        else:
            cnt += 1
    if (chk_no_current_id == True) or (chk_delete == False) :
        print("No Deleting <3")
    elif chk_delete:
        print("Done  >_<  <3")
def display_admin():
    print("Students Database XD")
    for i in Student_Data:
        for key , value in i.items():
            print(key ," --> ",value)
        print("----------------------------")

def give_access():
    print(Student_Data)
    cnt = 0
    chk_no_current_id = True
    access_id = int(input("Enter Student ID to Give Access or zero to exit: "))
    for i in Student_Data:
        if i["ID"] == access_id:
            chk_no_current_id = False
            confirm_access = input("Press Y to confirm or N to cancel: ")
            if confirm_access == "Y" or confirm_access == "y":
                Admin_Data.append(Student_Data[cnt])
                print(f"Now {Student_Data[cnt]['Name']} Have direct access to the Admin Page !")
        else:
            cnt += 1
    if chk_no_current_id:
        print("You Did Nothing!")
def admin():
    username = input("Username: ")
    password = input("Password: ")
    for i in Admin_Data:
        if i["username"] == username and i["password"] == password:
            while(True):
                print("1- Add Student")
                print("2- Edit on Student Information")
                print("3- Delete Student")
                print("4- Display Students Information")
                print("5- Give Access to Student (staff member)")
                print("6- Back")
                try:
                    start_num = int(input("Enter a Number: "))
                    if start_num == 1:
                        add_student()
                    elif start_num == 2:
                        edit_student()
                    elif start_num == 3:
                        delete_student()
                    elif start_num == 4:
                        display_admin()
                    elif start_num == 5:
                        give_access()
                    elif start_num == 6:
                        return 0;
                except:
                    print("Please enter Number of these!")

    print("Wrong password or username!")
    admin()


#-------------------------------------------------------
def student():
    print("Username = Name + ID")
    username = input("Username: ")  # username is ( name + id )
    password = input("Password: ")
    cnt = 0
    for i in Student_Data:
        if i["username"] == username and i["password"] == password:
            while (True):
                print("1- View Information")
                print("2- Change Password")
                print("3- Back")
                try:
                    start_num = int(input("Enter a Number: "))
                    if start_num == 1:
                        display_student(i)
                    elif start_num == 2:
                        chanege_password(i,cnt)
                    elif start_num == 3:
                        return 0;
                except:
                    print("Please enter Number of these!")

        else:
            cnt += 1

    print("Wrong password or username!")
    student()

def display_student(i):
    for key, value in i.items():
        print(key, " --> ", value)
    print("---------------------------------")
def chanege_password(i,cnt):
    chk_old_pass = input("Enter your old Password: ")
    new_pass = input("Enter a new password: ")
    if chk_old_pass != i["password"]:
        print("Wrong password!")
        chanege_password(i,cnt)
    else:
        Student_Data[cnt]["password"] = new_pass
#-------------------------------------------------------
def start():
    while(True):
        print("1- Admin Page")
        print("2- Student Page")
        print("3- Exit")
        try:
            start_num = int(input("Enter a Number: "))
            if start_num == 1:
                admin()
            elif start_num == 2:
                student()
            elif start_num == 3:
                print("Good Bye <3")
                return 0
        except:
            print("Please enter Number of these!")
start()


