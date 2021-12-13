student_details_dict = {}
module_details_dict = {}

class Program_maneger:
    try:
        global module_details_dict
        global student_details_dict


        def init(self):
            self.Program_maneger_menu()
            pass
        def Program_maneger_menu(self):
            print("Here are your options, Program_maneger! \n 1. Create module\n 2. Read module\n 3. update Module\
            \n 4. Delete module\n 5. Create student\n 6. View student\n 7. update student\
            \n 8. delete student\n 9. Exit")
            i = int(input("Please enter your choice\n"))
            while(i not in range(1,9)):
                if i == 9:
                    login()
                    break
                else:
                    print("Please enter a valid option!\n")
                    i = int(input("Please enter your choice, and make sure it's between 1 to 10\n"))
            else:     
                if i == 1:
                    self.create_module()
                    self.Program_maneger_menu()
                elif i == 2:
                    self.Read_module()
                    self.Program_maneger_menu()
                elif i == 3:
                    self.update_module()
                    self.Program_maneger_menu()
                elif i == 4:
                    self.delete_module(input("Please enter delete module to be deleted!\n"))
                    self.Program_maneger_menu()
                elif i == 5:
                    self.create_student()
                    self.Program_maneger_menu()
                elif i == 6:
                    self.view_student()
                    self.Program_maneger_menu()
                elif i == 7:
                    self.update_student()
                    self.Program_maneger_menu()
                elif i == 8:
                    self.delete_student(input("Please enter contact number of the student to be deleted!\n"))
                    self.Program_maneger_menu()
        
        def create_module(self):
            print("Okay Program_maneger, let's create a new module!\n")
            num = input("Please enter the module name to check if module does not exist!\n")
            while num in module_details_dict:
                print("Sorry it seems like the module already exists, would you like to update this instead?\n")
                break
            else:
                module_details_dict[num] = {}
                print("Okay seems like the module doesn't exist. Enter the details!\n")
                module_ID = input("Please enter Module ID!\n")
                module_details_dict[num]["Module ID"] = module_ID 
                module_name = input("Please enter Module name!\n")
                module_details_dict[num]["Module Name"] = module_name
                Start_date = input("Please enter Start_date!\n")
                module_details_dict[num]["Start_date"] = Start_date
                End_date = input("Please enter end_date!\n")
                module_details_dict[num]["end_date"] = End_date
                units = input("Please enter units!\n")
                module_details_dict[num]["units"] = units
        def update_module(self):
            print("Okay Program_maneger, let's update module!\n")
            num = input("Please enter the module name to check if module does not exist!\n")
            module_details_dict[num] = {}
            module_ID = input("Please enter Module ID!\n")
            module_details_dict[num]["Module ID"] = module_ID 
            module_name = input("Please enter Module name!\n")
            module_details_dict[num]["Module Name"] = module_name
            Start_date = input("Please enter Start_date!\n")
            module_details_dict[num]["Start_date"] = Start_date
            End_date = input("Please enter end_date!\n")
            module_details_dict[num]["Start_date"] = End_date
            units = input("Please enter units!\n")
            module_details_dict[num]["units"] = units


                
        def Read_module(self):
            check = input("Please enter the module name!\n")
            if check in module_details_dict:
                print("The Details for modules are: ")
                for detail in module_details_dict[check]:
                    if type(module_details_dict[check][detail]) != dict:
                        print('{} : {}'.format(detail, module_details_dict[check][detail]))
                    else:
                        print(detail + ":")
                        for j in module_details_dict[check][detail]:
                            print('{} : {}'.format(j, module_details_dict[check][detail][j]))
            else: 
                print("Sorry, it seems the Module doesn't exist!\n")

            print("Lets go back to the Main Menu!\n\n") 
        
        def delete_module(self, num):
            if num in module_details_dict:
                del module_details_dict[num]
            else:
                print("The module doesn't exist\n")
            print("Lets go back to the Main Menu!\n\n") 
        
        def create_student(self):
            print("Okay Program_maneger, let's create a new student!\n")
            num = input("Please enter the contact number to check if student does not exist!\n")
            while num in student_details_dict:
                print("Sorry it seems like the student already exists, would you like to update this instead?\n")
                break
            else:
                student_details_data = {}
                print("Okay seems like the student doesn't exist. Enter the details!\n")
                full_name = input("Please enter Full Name of student!\n")
                student_details_data["Full Name"] = full_name
                email = input("Please enter Email ID of student!\n")
                student_details_data["Email ID"] = email
                password = input("Please enter password ID of student!\n")
                student_details_data["password"] = password
                module_id = input("Please enter module_id of student!\n")
                student_details_data["module_id"] = module_id
                student_details_dict[num]=student_details_data
        def update_student(self):
            print("Okay Program_maneger, let's create a new student!\n")
            num = input("Please enter the contact number to check ifstudent does not exist!\n")
            if num not in student_details_dict:
                print("Sorry it seems like the student does not exists. Try again!\n")
            else:
                print("Okay seems like the student doesn't exist. Enter the details!\n")
                full_name = input("Please enter Full Name of student!\n")
                student_details_dict[num]["Full Name"] = full_name
                email = input("Please enter Email ID of student!\n")
                student_details_dict[num]["Email ID"] = email
                password = input("Please enter password ID of student!\n")
                student_details_dict[num]["password"] = password
                module_id = input("Please enter module_id of student!\n")
                student_details_dict[num]["module_id"] = module_id
        
        def view_student(self):
            check = input("Please enter the Contact Number of the student!\n")
            if check in student_details_dict:
                print("The Details for student are: ")
                for detail in student_details_dict[check]:
                    if type(student_details_dict[check][detail]) != dict:
                        print('{} : {}'.format(detail,student_details_dict[check][detail]))
                    else:
                        print(detail + ":")
                        for j in  student_details_dict[check][detail]:
                            print('{} : {}'.format(j,student_details_dict[check][detail][j]))
            else: 
                print("Sorry, it seems the student doesn't exist!\n")

            print("Lets go back to the Main Menu!\n\n")
        
        def delete_student(self, num):
            if num in student_details_dict:
                del student_details_dict[num]
            else:
                print("The student doesn't exist\n")
                print("Lets go back to the Main Menu!\n\n")
    except:
        print("Something went wrong")
        
class student:
    def init(self):
        self.num = input("Please enter contact number.")
        if self.num in student_details_dict:
            print("Welcome, {} to EDYODA LMS!".format(student_details_dict[self.num]['Full Name']))
            self.student_menu()
        else:
            print("Sorry it seems, you are not a student!\n Please ask the Program Manager to add your details!")
    def student_menu(self):
        while(True):
            print("Please choose one of the following options!\n1. today Schedule\n2. View My Modules\n 3.Update Profile\n 4. Exit Menu.")
            i = int(input())
            if i == 1:
                self.view_student_module()
                self.student_menu()
            elif i ==2:
                self.view_student_module()
                self.student_menu()
            elif i==3:
                self.update_profile()
                self.student_menu()
            elif i==4:
                break
            else:
                print("Please choose valid option")
    def view_student_module(self):
        check = input("Please enter the Your Contact Number!\n")
        if check in module_details_dict:
            print("The Details for student are: ")
            for detail in module_details_dict[check]:
                if type(module_details_dict[check][detail]) != dict:
                    print('{} : {}'.format(detail,module_details_dict[check][detail]))
                else:
                    print(detail + ":")
                    for j in  module_details_dict[check][detail]:
                        print('{} : {}'.format(j,module_details_dict[check][detail][j]))
        else:
            print("Student not exists!")
    def update_profile(self):
        num = input("Please enter your contact number to check if student does not exist!\n")
        if num not in student_details_dict:
            print("ok lets go!\n")
        else:
            print(" Enter the details!\n")
            full_name = input("Please enter Full Name of student!\n")
            student_details_dict[num]["Full Name"] = full_name
            email = input("Please enter Email ID of student!\n")
            student_details_dict[num]["Email ID"] = email
            password = input("Please enter password ID of student!\n")
            student_details_dict[num]["password"] = password
            module_id = input("Please enter module_id of student!\n")
            student_details_dict[num]["module_id"] = module_id

            

def login():

    print("------Welcome to EDYODA LMS!------")
    i = int(input("Please enter one of the following!\n1. Program_maneger\n2. student\n3. Exit\n"))
    while(True):
        if i == 1:
            obj = Program_maneger()
            obj.Program_maneger_menu()
        else:
            obj = student()
            obj.student_menu()

login()

