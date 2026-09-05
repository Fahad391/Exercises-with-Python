try:
    class Employee:
        def __init__(self, name, designation, salary):
            self.name = name
            self.designation = designation
            self.salary = salary

            if not isinstance(self.salary, (float)):
                raise ValueError("Salary must be float")

        def display_employee_data(self):
           return f"Name: {self.name} | Designation: {self.designation} | Salary: {self.salary} BDT"


    class Company:
        def __init__(self, company_Name):
            self.company_name = company_Name
            self.employees = []

        def add_employee(self, employee):
            self.employees.append(employee)

            with open("Lists.csv", 'a') as file:
                file.write(f"{employee.name},{employee.designation},{employee.salary}\n")

        def show_employees(self):
            print(f"{self.company_name}'s Employees\n")
            with open("Lists.csv", 'r') as file:
                for record in file:
                    record = record.strip()
                    if not record:
                        continue
                    name, designation, salary = record.split(',')
                    employee = Employee(name, designation, float(salary))
                    print(employee.display_employee_data())

    employee1 = Employee("Alice", "Manager", 80000.0)
    employee2 = Employee("Bob", "Developer", 60000.0)
    employee3 = Employee("Vijay", "System Architect", 75980.5)

    company = Company("XYZ")
    #company.add_employee(employee1)
    #company.add_employee(employee2)
    #company.add_employee(employee3)

    company.show_employees()
    #print(employee3.display_employee_data())


except Exception as error:
    print(error)