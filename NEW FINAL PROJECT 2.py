employee_list=[]
def write_into_txt():
    employee_list =[]
    with open("employee_list.txt","w") as f:
        for item in list:
            f.write(str(item)+"\n")

def read_from_txt():
    with open("employee_list.txt", 'r') as r:
        for item in r:
            employee_list.append(int(item.strip()))

            

def addEmployee():
    employee_name = input("Enter employee name: ")
    employee_ssn = input("Enter employee SSN: ")
    employee_phone = input("Enter employee phone: ")
    employee_email = input("Enter employee email: ")
    employee_salary = input("Enter employee salary: ")
    employee=[employee_name,employee_ssn,employee_phone,employee_email,employee_salary]
    employee_list.append(employee)
    write_into_txt()


def view_employees():
    read_from_txt()
    for index in range(len(employee_list)):
        employee_name=employee_list[index][0]
        employee_ssn=employee_list[index][1]
        employee_phone=employee_list[index][2]
        employee_email=employee_list[index][3]
        employee_salary=employee_list[index][4]
        #output

        header = "----------------------------- " + employee_name + " -----------------------------"

        print(header)
        print("SSN: " + employee_ssn)
        print("Phone:"+ employee_phone)
        print ("Email:" + employee_email)
        print ("Salary:" + employee_salary)
        print("-" * len(header))

def search_employees():
    read_from_txt()
    ssn=input("Please enter the Social Security Number of Employee: ")
    found_empplyee=None
    for employee in employee_list:
        if employee[1]==ssn:
            found_empplyee=employee      
            header = "----------------------------- " + employee[0] + " -----------------------------"

            print(header)
            print("SSN: " + employee[1])
            print("Phone:"+ employee[2])
            print ("Email:" + employee[3])
            print ("Salary:" + employee[4])
            print("-" * len(header))
            edit = input('would you like to edit this information? yes or no:')
            if edit == 'yes':
                print("Select 1 to change Name")
                print("Select 2 to change SSN")
                print('Select 3 to change phone number')
                print('Select 4 to change email address')
                print('Select 5 to change salary')

                modify = input()
                if modify =='1':
                    employee[0]= input("Enter new name: ")
                    print("Name changed to ", employee[0])
                elif modify =="2":
                    employee[1]= input("Enter new SSN: ")
                    print("SSN changed to ", employee[1])
                elif modify =="3":
                    employee[2]= input("Enter new phone number: ")
                    print("Phone number changed to ", employee[2])
                elif modify =="4":
                    employee[3]= input("Enter new email address: ")
                    print("Email Address changed to ", employee[3])
                elif modify =="5":
                   employee[5]= input("Enter new Salary")
                   print("Salary changed to ", employee[4])
                else:
                    print('Action not found')

            else:
                print('Thank you have a great day!')
            
            
                    
            break
    return found_empplyee

def menu():
    emp_num = 0

    while True:
        print(20 * '_', 'Employee Management System', 20 * '_')
        print('please select an option')
        print('1. Add Employees')
        print('2. Edit Employees')
        print('3. View All Employees')
        print('4. Exit')
        print(68 * '_')
        process = input('Please Make Your Selection? 1 - 4: ')

        if process == '1':
            addEmployee()  # assuming this function is defined elsewhere
        elif process == '2':
            print(search_employees())  # assuming this function is defined elsewhere
        elif process == '3':
            view_employees()  # assuming this function is defined elsewhere
        elif process == '4':
            print('Thank You! Have a great day!')
            break  # exit the loop if the user enters '4'
        else:
            print('Invalid input. Please enter a number between 1 and 4.')

menu()
