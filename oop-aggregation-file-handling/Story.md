# Project: Employee Management System

## Introduction

This project started as a practice exercise.

I wanted to combine three Python concepts I had been learning:

* **Object-Oriented Programming (OOP)**
* **Aggregation**
* **File Handling**

Instead of practicing these concepts separately, I wanted to build one small program where they could work together.

My basic plan was simple:

> Create employees, put them under a company, and save their information in a file so I could read it later.

I wrote the code myself. When I got stuck, I used ChatGPT mainly to understand **what was happening in my code and why something was not working**. After understanding the problem, I tried to apply the fix to my own code rather than simply replacing my code with a solution.

This is how the project developed.

---

# 1. What I Planned First

Before writing much code, I had a basic structure in mind.

I wanted two main classes:

```text
Company
   │
   ├── Employee
   ├── Employee
   └── Employee
```

The idea was that a `Company` would have multiple `Employee` objects.

I also wanted employee information to be saved in a CSV file:

```text
Employee Object
      ↓
Company
      ↓
CSV File
```

Later, the program would read the CSV file and display the employees again.

So my overall idea became:

```text
Create Employee
       ↓
Add Employee to Company
       ↓
Save Employee Data to CSV
       ↓
Read CSV Later
       ↓
Recreate Employee Object
       ↓
Display Employee
```

At the beginning, I didn't have all of this figured out in detail. I developed the structure as I coded.

---

# 2. I Started With the Employee Class

The first thing I thought about was:

**What information should an employee have?**

For my practice, I decided on:

* Name
* Designation
* Salary

So I started with:

```python
class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
```

This part was straightforward.

Then I wanted to practice a little validation as well. I decided that the salary should be a `float`.

So I added:

```python
if not isinstance(self.salary, (float)):
    raise ValueError("Salary must be float")
```

I also created a method for displaying the employee information:

```python
def display_employee_data(self):
    return f"Name: {self.name} | Designation: {self.designation} | Salary: {self.salary} BDT"
```

At this stage, I had a basic `Employee` class that could create and display employee objects.

---

# 3. Then I Thought About the Company

The next question was:

**How should multiple employees belong to a company?**

I wanted to practice **Aggregation**, so I decided that the company should maintain a collection of employee objects.

I created:

```python
class Company:
    def __init__(self, company_Name):
        self.company_name = company_Name
        self.employees = []
```

The important part here was:

```python
self.employees = []
```

My intention was for this list to contain actual `Employee` objects.

Then I created some employees:

```python
employee1 = Employee("Alice", "Manager", 80000.0)
employee2 = Employee("Bob", "Developer", 60000.0)
employee3 = Employee("Vijay", "System Architect", 75980.5)
```

And created a company:

```python
company = Company("XYZ")
```

The structure I was aiming for was:

```text
Company Object
      │
      └── employees
             │
             ├── Employee Object
             ├── Employee Object
             └── Employee Object
```

This was where the OOP and Aggregation part of the project started taking shape.

---

# 4. Adding `add_employee()`

After creating the classes, I needed a way to add employees to the company.

I wrote:

```python
def add_employee(self, employee):
    self.employees.append(employee)
```

This was the basic aggregation relationship.

When I do:

```python
company.add_employee(employee1)
```

the `Employee` object is added to the company's employee list.

So I understood it as:

```text
employee1
   │
   ▼
Company.employees
   │
   └── [employee1]
```

The employee object still exists independently. The company simply keeps a reference to it.

---

# 5. My Next Plan: Save Employees to a File

Once the basic OOP structure was working, I wanted to add **File Handling**.

I didn't want the employee information to disappear when the program stopped.

So I decided to save employee information into a CSV file.

I changed my `add_employee()` method to:

```python
def add_employee(self, employee):
    self.employees.append(employee)

    with open("Lists.csv", 'a') as file:
        file.write(f"{employee.name},{employee.designation},{employee.salary}\n")
```

Now the method had two responsibilities:

```text
add_employee()
      │
      ├── Add Employee object to list
      │
      └── Save Employee data to CSV
```

For example:

```python
company.add_employee(employee1)
```

would store the object in memory and write something like:

```text
Alice,Manager,80000.0
```

into `Lists.csv`.

This was my first real combination of **Aggregation + File Handling**.

---

# 6. Where I Got Stuck: Reading the File

After writing employee information to the CSV, I wanted to read it back.

My thinking at that point was roughly:

> If I saved employees into the file, I should be able to read the employees from the file.

So my first approach was something like:

```python
with open("Lists.csv", 'r') as file:
    records = file.read()

    for employee in records:
        print(employee.display_employee_data())
```

I expected `employee` to represent an employee.

But the code obviously didn't behave that way.

This was one of the points where I used ChatGPT.

I wasn't looking for a completely different program. I wanted to understand:

**What exactly is `file.read()` giving me?**

---

# 7. What I Learned About `file.read()`

The important thing I learned was that:

```python
file.read()
```

returns the contents of the file as **one string**.

For example, if the file contains:

```text
Alice,Manager,80000.0
Bob,Developer,60000.0
```

then `file.read()` gives me text representing the whole file.

So when I wrote:

```python
for employee in records:
```

Python was not giving me employee objects.

It was iterating through the characters of the string.

Conceptually:

```text
"Alice,Manager,80000.0"
 ↓
A
l
i
c
e
,
M
a
n
...
```

That immediately explained why this idea was wrong:

```python
employee.display_employee_data()
```

There was no `Employee` object there.

There was only a character.

This was an important point in my learning because I started understanding the difference between:

```text
Python Object
```

and:

```text
Data stored inside a file
```

They are not automatically the same thing.

---

# 8. I Changed the Way I Read the File

After understanding that `file.read()` returns text, I changed my approach.

Instead of reading the entire file as one string and iterating through its characters, I used:

```python
for record in file:
```

This allows me to process the file **line by line**.

For example:

```text
Alice,Manager,80000.0
Bob,Developer,60000.0
Vijay,System Architect,75980.5
```

could be processed as:

```text
Record 1 → Alice,Manager,80000.0
Record 2 → Bob,Developer,60000.0
Record 3 → Vijay,System Architect,75980.5
```

That was much closer to what I actually needed.

---

# 9. Turning the File Data Back Into an Employee

There was still another problem.

Even though I was now reading one line at a time, the line was still just text.

For example:

```text
Alice,Manager,80000.0
```

is not automatically:

```python
Employee("Alice", "Manager", 80000.0)
```

So I needed to reconstruct the object.

I moved toward:

```python
for record in file:
    record = record.strip()

    name, designation, salary = record.split(',')

    employee = Employee(name, designation, float(salary))

    print(employee.display_employee_data())
```

This became one of the most important pieces of logic in the project.

The process was now:

```text
CSV File
   ↓
Read one line
   ↓
Remove newline
   ↓
Split values
   ↓
name
designation
salary
   ↓
Convert salary to float
   ↓
Create Employee object
   ↓
Display object
```

For example:

```text
Alice,Manager,80000.0
```

became:

```python
name = "Alice"
designation = "Manager"
salary = "80000.0"
```

Then:

```python
float(salary)
```

converted:

```text
"80000.0"
```

into:

```python
80000.0
```

Finally:

```python
Employee(name, designation, float(salary))
```

created a new `Employee` object.

This was the point where I understood that reading data from a file and getting an object back are **two separate steps**.

---

# 10. Another Problem Appeared

After getting the main reading logic working, I encountered another error:

```text
not enough values to unpack (expected 3, got 1)
```

The line causing the problem was:

```python
name, designation, salary = record.split(',')
```

I knew my normal records contained three values:

```text
Alice,Manager,80000.0
```

So I had to figure out why Python was sometimes finding only one value.

I used ChatGPT again to understand what was happening rather than replacing the entire logic.

The problem was an empty line in the file.

For an empty line:

```python
record.strip()
```

could produce:

```python
""
```

And:

```python
"".split(',')
```

doesn't give me three pieces of employee information.

So I added:

```python
record = record.strip()

if not record:
    continue
```

Now the logic became:

```text
Read line
   ↓
Remove whitespace/newline
   ↓
Is it empty?
   │
   ├── Yes → skip it
   │
   └── No → split the record
```

This was a useful debugging lesson for me.

The problem wasn't always with the code's main idea.

Sometimes the **input data itself** needs to be considered.

---

# 11. I Also Noticed Duplicate Records

While testing the program, I noticed that the same employees could appear multiple times in the CSV.

At first, this looked like another program problem.

Then I looked at how I was opening the file:

```python
open("Lists.csv", 'a')
```

The `'a'` means **append mode**.

That means Python doesn't replace the existing contents.

It adds the new data to the end.

So if I repeatedly run:

```python
company.add_employee(employee1)
```

I can get:

```text
Alice,Manager,80000.0
Alice,Manager,80000.0
Alice,Manager,80000.0
```

The program isn't randomly duplicating the employee.

I had explicitly told Python to append new records.

This helped me understand the difference between:

```text
Program logic
```

and:

```text
Persistent data already stored in the file
```

The CSV keeps its previous contents even after the program stops.

---

# 12. Where the Project Ended Up

After working through these problems, I ended up with this version:

```python
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
```

The final code is not the result of starting with a perfect design.

It is the result of gradually understanding what each part of the program was actually doing.

---

# 13. What I Actually Practiced

Although the project is small, I ended up practicing several different concepts together.

### Object-Oriented Programming

I created:

```python
class Employee:
```

and:

```python
class Company:
```

I created objects using those classes and worked with their attributes and methods.

### Aggregation

The company maintains a list of employee objects:

```python
self.employees = []
```

and adds employee objects using:

```python
self.employees.append(employee)
```

The employees can exist independently from the company, which is the relationship I wanted to practice.

### File Handling

I practiced writing data:

```python
with open("Lists.csv", 'a') as file:
```

and reading data:

```python
with open("Lists.csv", 'r') as file:
```

### String Processing

I practiced:

```python
strip()
```

and:

```python
split(',')
```

to process the data coming from the file.

### Type Conversion

Because the CSV contains text, salary has to be converted back:

```python
float(salary)
```

### Object Reconstruction

I learned that reading employee information from a CSV does not automatically create an `Employee` object.

I have to explicitly reconstruct it:

```python
employee = Employee(name, designation, float(salary))
```

### Exception Handling

I also practiced:

```python
try:
    ...
except Exception as error:
    print(error)
```

to catch errors during execution.

---

# 14. How I Used ChatGPT During the Project

I used ChatGPT as a **debugging and learning tool**.

I did not start by asking:

> "Write the whole employee management system for me."

Instead, I wrote the code and brought specific problems when I got stuck.

For example, when my file-reading logic wasn't working, I needed to understand why:

```python
file.read()
```

wasn't giving me employee objects.

ChatGPT helped me understand that I was actually dealing with a string.

Then I changed my own approach.

When I got:

```text
not enough values to unpack
```

I used ChatGPT to understand why the unpacking was failing.

After learning that an empty line could produce the problem, I added:

```python
if not record:
    continue
```

myself.

Similarly, when I noticed duplicate records, I investigated the meaning of:

```python
'a'
```

in:

```python
open("Lists.csv", 'a')
```

and understood that the file was being opened in append mode.

So my process was generally:

```text
Write Code
    ↓
Run Code
    ↓
Encounter Problem
    ↓
Ask ChatGPT "Why?"
    ↓
Understand the Concept
    ↓
Apply the Fix Myself
    ↓
Run Again
    ↓
Continue Building
```

That was the main way I used ChatGPT throughout this project.

---

# 15. What Changed From My First Idea to the Final Program

My original idea was simple:

```text
Company → Employees → File
```

But while implementing it, I learned that there are actually several layers involved.

The final flow became:

```text
                 MEMORY
                    │
                    ▼
             Employee Object
                    │
                    ▼
             Company Object
                    │
                    ├── employees list
                    │
                    ▼
              add_employee()
                    │
                    ▼
              CSV File
                    │
              STORED AS TEXT
                    │
                    ▼
              show_employees()
                    │
                    ▼
             Read line by line
                    │
                    ▼
                strip()
                    │
                    ▼
                split(',')
                    │
                    ▼
          Convert salary to float
                    │
                    ▼
          Reconstruct Employee
                    │
                    ▼
              Display Object
```

The important part for me was understanding what happens at each transition.

---

# Final Reflection

This project started with a relatively simple goal: practice **OOP, Aggregation, and File Handling together**.

I didn't know exactly how every part would work when I started.

I wrote the classes first, then added the company relationship, then added file handling. Along the way, I ran into problems with reading files, strings versus objects, empty records, data conversion, and duplicate records.

Whenever I got stuck, I used ChatGPT to understand the specific problem.

The important part was that I didn't want ChatGPT to simply replace my code. I wanted to understand what was happening so I could make the changes myself.

The biggest concept I took from this project was the difference between **an object in memory and data stored in a file**.

An object like:

```python
Employee("Alice", "Manager", 80000.0)
```

exists as a Python object in memory.

The CSV only stores something like:

```text
Alice,Manager,80000.0
```

When I read that CSV later, I don't automatically get my original object back. I have to read the text, process it, and reconstruct the object.

Understanding that connection made the relationship between **OOP, Aggregation, and File Handling** much clearer to me.

This project may be small, but it was useful practice because I built it progressively, encountered real errors, understood why they happened, and fixed them as I went.
