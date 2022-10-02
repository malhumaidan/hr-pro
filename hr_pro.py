class Employee:
   #Employee class here
    def __init__(self, name, age, salary, employment_years):
        self.name = "name: " + name
        self.age = "age: " + str(age)
        self.salary = "salary: " + str(salary)
        self.employment_years = "Working Years: " + str(employment_years)
    
    def __str__(self):
        return f"{self.name} , {self.age}, {self.salary}, {self.employment_years}"


    def get_annual_salary(self, salary):
        self.salary = salary*12
        print(f"{self.salary}")



employee = Employee("Moh", 23, 10, 5)
# print(employee.get_annual_salary(10))
# print(employee.__str__())

class Manager(Employee):
    bonus_percentage = 0.15
    #Manager class here
    def __init__(self, name, age, salary, employment_years):
         super().__init__(name, age, salary, employment_years)

    def get_bonus(self):
        self.bonus_percentage * self.salary
        return True

    def __str__(self):
         return super().__str__()
        
manager = Manager("Manager", 54, 20, 9)
# print(manager.__str__())
# print(manager.get_bonus())

employees_list = [employee]
managers_list = [manager]
# print(employees_list)

print("Welcome to HR Pro")
print("Options:")

options = ["Show Employees", "Show Managers", "Add An Employee", "Add A Manager", "Exit"]

def show_options(options):

    
    for number, options in enumerate(options,1):
        print(number, options)

print(show_options(options))

user_option = int(input("What would you like to do? "))

if user_option == 1:
    print("----------------")
    print(" ")

    for employee in employees_list:
        print(employee)
    print("----------------")

if user_option == 2:
    print("----------------")
    print(" ")

    for manager in managers_list:
        print(manager)
    print("----------------")


if user_option == 3:
    
    employee_name = input("Enter a name: ")
    employee_age = int(input("Enter Age: "))
    employee_salary = int(input("Enter salary: "))
    employee_employment_years = int(input("Enter xp: "))
    employee = Employee(employee_name, employee_age, employee_salary, employee_employment_years)
    employees_list.append(employee)
    

if user_option == 4:
    manager_name = input("Enter a name: ")
    manager_age = int(input("Enter Age: "))
    manager_salary = int(input("Enter salary: "))
    manager_employment_years = int(input("Enter xp: "))
    manager_bonus_percentage = float(input("Enter bonus percentage: "))
    managers = "name: " + manager_name, "age: " + str(manager_age), "salary: " + str(manager_salary), "Working Years " + str(manager_employment_years), "Bonus: " + str(manager_bonus_percentage)
    managers_list.append(managers)
    print(managers_list)

def main():
	# main code here
    ...
    

if __name__ == '__main__':
	main()
