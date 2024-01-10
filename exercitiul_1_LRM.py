class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = "F02" + department
        Manager.mgr_count += 1

    def display_employee(self):
        print("Name: ", self.name, ", Department: ", self.department)



manager1 = Manager("John Doe", 50000, "Media")
manager2 = Manager("Alice Smith", 60000, "Finance")
manager3 = Manager("Bob Johnson", 55000, "IT")


manager1.display_employee()
manager2.display_employee()
manager3.display_employee()


employee1 = Employee("Eva Brown", 45000)
employee2 = Employee("Charlie White", 48000)

employee1.display_employee()
employee2.display_employee()


print(f"Employee Count: {employee1.empCount}")
print(f"Manager Count: {manager1.mgr_count}")
