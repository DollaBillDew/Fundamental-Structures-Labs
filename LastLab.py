
def ID():
    while True:
        EmployeeID = input("Enter Employee ID: ")
        
        if EmployeeID == "":
            print("Employee ID cannot be empty. Enter again.")
        elif len(EmployeeID) > 7:
            print("Employee ID should be less than or equal to 7. Enter again.")
        elif EmployeeID.isdigit():
            break
        else:
            print("The employee ID has non numeric characters. Enter again")
            
    return EmployeeID

def name():
    while True:
        EmployeeName = input("Enter Employee name: ")

        if EmployeeName.strip() == "":
            print("Employee name can not be empty.")
        elif EmployeeName.lower().replace("-", "").replace("'", "").replace(" ", "").isalpha():
            break
        else:
            print("Enter correct employee name.")
            
    return EmployeeName

def email():
    while True:
        EmployeeEmail = input("Enter Employee email: ")
        
        if len(set("!\"'#$%^&*()= +,<>/?;:[]{}\\").intersection(set(EmployeeEmail))) > 0:
            print("Do not use any of these characters: ! \" ' # $ % ^ & * ( ) = + , < > / ? ; : [ ] { } \\. Try again.")
        elif EmployeeEmail.strip().replace("@", "").replace(".", "").replace("_", "").isalnum():
            break
        else:
            print("Try again.")
            
    return EmployeeEmail

def salary():
    while True:
        EmployeeSalary = input("Enter salary: ")

        try:
            EmployeeSalary = float(EmployeeSalary)
            if EmployeeSalary < 18 and EmployeeSalary > 27:
                print("Salary should be between 18 and 27")
            else:
                break
        except:
            print("The digit is not a floating point.")
            
    return EmployeeSalary
employees = list()
while True:
    EmployeeID = ID()
    EmployeeName = name()
    EmployeeEmail = email()
    EmployeeSalary = salary()
    
    employee = {
        "id": EmployeeID,
        "name": EmployeeName,
        "email": EmployeeEmail,
        "salary": EmployeeSalary,
    }
    
    employees.append(employee)
    
    quit = input("Do you want to quit? Y/N ").lower()
    if quit == "y":
        break
for employee in employees:
    employee["name"] = "IT Department" + employee["name"]
    employee["salary"] = employee["salary"] * 1.3
    
print(employees)