employees={101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}
def add_employee(employees):
    emp_id=int(input("Enter employee id :"))
    name=str(input("Enter employee name :"))
    age=int(input("Enter age :"))
    department=str(input("Enter departmanet :"))
    salary=int(input("Enter Salary :"))
    if emp_id in employees:
        print("The id already exist :")
    else:
        employees[emp_id]={'name':name,'age':age,'department':department,'salary':salary}
        
def delete_Employee(employees):
    emp_id=int(input("Enter employee id to delete :"))
    if emp_id not in employees:
        print("The id doesn't exit :")
    else:
        employees.pop(emp_id)
        
def update_employee(employees):
    emp_id=int(input("Enter id to update :"))
    if emp_id not in employees:
        print("The id doesn't exit :")
    else:
        x=int(input("""
                Enter 1 to update slary:
                Enter 2 to update age :
                Enter 3 to update department :"""))
        if x==1:
            salary=int(input("Enter new salary :"))
            employees[emp_id]['salary']=salary
        elif x==2:
            age=int(input("Enter new age :"))
            employees[emp_id]['age']=age
        elif x==3:
            department=str(input("Enter new department :"))
            employees[emp_id]['department']=department
def display_employee(employees):
    
    emp_id=int(input(("Enter employee id to display :")))
    if emp_id not in employees:
        print("The id doesn't exit :")
    else:
        print(f"The employee data={employees[emp_id]}")
        
def displayall(employees):
    for i in employees:
        print(f"{i} : {employees[i]}") 
    
    
i=int(input("Enter 0 to start :"))
while(i!=-1):
    i=int(input(f""" 
            Enter 1 to add :
            Enter 2 to delete:
            Enter 3 to dislay one employee:
            Enter 4 to display all:
            Enter 5 to update :
            Enter -1 to exit:"""))
    if i==1:
        add_employee(employees)
    elif i==2:
        delete_Employee(employees)
    elif i==3:
        display_employee(employees)
    elif i==4:
        displayall(employees)
    elif i==5:
        update_employee(employees)
    elif i==-1:
        print("Thank you:")
        break
    else:
        print("Invalid entry try again :")
        
        
        
        