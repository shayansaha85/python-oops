class Employee:
    # PROPERTIES
    name = ""
    employee_id = 0
    salary = 0
    
    # PARAMETERIZED CONSTRUCTOR
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    # METHODS / BEHAVIORS
    def seeinfo(self):
        print("DETAILS")
        print("="*15)
        print("Name :",self.name)
        print("Employee ID :",self.employee_id)
        print("Salary :",self.salary)
        print()
        
        
        
e1 = Employee("Shayan Saha", 101, 56000)
e2 = Employee("Pranjit Chowdhury", 102, 53000)

e1.seeinfo()
e2.seeinfo()