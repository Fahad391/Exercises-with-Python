# Project: Employee Management System

## Introduction

This project started as a practice exercise to combine some of the Python concepts I learned, especially **Object-Oriented Programming (OOP), Aggregation, and File Handling**.

I wanted to see whether I could take these concepts and make them work together in one small program instead of practicing each concept separately.

I wrote the code myself. Whenever I got stuck, I used ChatGPT mainly to understand **why something was not working**, rather than simply asking it to write the solution for me. I tried to fix each problem myself after understanding the underlying concept.

This documentation tells the story of how I reached the final code that worked as planned.

---

## 1. Starting With the Employee Class

I first thought about what an employee should contain.

An employee has:

* A name
* A designation
* A salary

So I created an `Employee` class:

```python
class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary
```

I also wanted to practice validation, so I decided that the salary should be a `float`.

```python
if not isinstance(self.salary, (float)):
    raise ValueError("Salary must be float")
```

Then I created a method to display the employee's information:

```python
def display_employee_data(self):
    return f"Name: {self.name} | Designation: {self.designation} | Salary: {self.salary} BDT"
```

At this point, the `Employee` class was relatively straightforward.

---

## 2. Introducing the Company Class

Next, I wanted a `Company` that could contain multiple employees.

This was where I started applying **Aggregation**.

My idea was:

> A company has employees, but employees can exist independently of the company.

That led me to create:

```python
class Company:
    def __init__(self, company_Name):
        self.company_name = company_Name
        self.employees = []
```

The `employees` list would hold my `Employee` objects.

I then created several employee objects:

```python
employee1 = Employee("Alice", "Manager", 80000.0)
employee2 = Employee("Bob", "Developer", 60000.0)
employee3 = Employee("Vijay", "System Architect", 75980.5)
```

And created the company:

```python
company = Company("XYZ")
```

---

## 3. Adding File Handling

After getting the basic OOP structure working, I wanted to bring **file handling** into the project.

My idea was to save employee information into a CSV file so that the data would not exist only while the program was running.

I created an `add_employee()` method:

```python
def add_employee(self, employee):
    self.employees.append(employee)

    with open("Lists.csv", 'a') as file:
        file.write(f"{employee.name},{employee.designation},{employee.salary}\n")
```

This does two things:

1. Adds the employee object to the company's `employees` list.
2. Saves the employee's information into `Lists.csv`.

This was the point where aggregation and file handling started working together.

---

## 4. The First Major Problem

My first attempt at displaying employees from the file looked roughly like this:

```python
with open("Lists.csv", 'r') as file:
    records = file.read()
    for employee in records:
        print(employee.display_employee_data())
```

I expected `employee` to represent an employee.

It didn't.

The important thing I learned here was that **a CSV file contains text, not Python objects**.

When I used:

```python
file.read()
```

I got the entire file as a string.

Then:

```python
for employee in records:
```

was actually looping through the characters of that string.

So instead of getting:

```text
Employee object
Employee object
Employee object
```

I was effectively getting:

```text
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

This helped me understand an important difference between **stored data** and **objects in memory**.

---

## 5. Understanding Object Reconstruction

After understanding the problem, I changed my approach.

Instead of expecting the CSV file to give me an `Employee` object, I needed to:

1. Read a record from the CSV.
2. Separate the values.
3. Create an `Employee` object from those values.
4. Display that newly created object.

I moved toward:

```python
for record in file:
    name, designation, salary = record.strip().split(',')
    employee = Employee(name, designation, float(salary))
    print(employee.display_employee_data())
```

This was an important step in the project.

The CSV stores:

```text
Alice,Manager,80000.0
```

But my Python program reconstructs that information into:

```python
Employee("Alice", "Manager", 80000.0)
```

So the process became:

```text
CSV record
     ↓
Read text
     ↓
Split into values
     ↓
Create Employee object
     ↓
Display Employee object
```

That was something I wanted to understand rather than just make work.

---

## 6. The Next Error: "Expected 3, Got 1"

After getting the main logic working, I encountered another error:

```text
not enough values to unpack (expected 3, got 1)
```

The problematic line was:

```python
name, designation, salary = record.strip().split(',')
```

At first, it was confusing because the valid records clearly contained three values.

The problem turned out to be that the file contained an **empty line**.

For example:

```text
Alice,Manager,80000.0
Bob,Developer,60000.0
Vijay,System Architect,75980.5

```

For the empty line:

```python
record.strip()
```

became:

```python
""
```

And:

```python
"".split(',')
```

didn't produce three values.

So I added:

```python
record = record.strip()

if not record:
    continue
```

Now blank lines are ignored before trying to split the record.

This was another useful lesson: sometimes the error isn't necessarily in the main logic. **The input data itself can cause the error.**

---

## 7. Understanding the Duplicate Records Problem

Another issue I noticed was that employee records could appear multiple times in the CSV.

This was caused by using:

```python
open("Lists.csv", 'a')
```

The `'a'` means **append mode**.

So every time I run:

```python
company.add_employee(employee1)
```

the record gets added to the end of the existing file.

If I run the program several times, I can end up with:

```text
Alice,Manager,80000.0
Bob,Developer,60000.0
Vijay,System Architect,75980.5
Alice,Manager,80000.0
Bob,Developer,60000.0
Vijay,System Architect,75980.5
```

The program isn't randomly creating duplicate employees.

The duplicates are actually **stored in the CSV because I told Python to append new records**.

Understanding this distinction was important.

---

## 8. The Final Structure

After going through these problems, I ended up with the following version:

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

---

## 9. What I Learned From This Practice

This small project ended up teaching me more than I initially expected.

### OOP

I practiced creating classes and objects and separating responsibilities between `Employee` and `Company`.

### Aggregation

I practiced the idea that a `Company` can contain multiple `Employee` objects:

```python
self.employees = []
```

and:

```python
self.employees.append(employee)
```

The employees are separate objects; the company simply maintains a relationship with them.

### File Handling

I practiced:

```python
open("Lists.csv", 'a')
```

for saving data and:

```python
open("Lists.csv", 'r')
```

for reading it.

### CSV Data

I learned that CSV data is just text when read normally. If I want Python objects from that data, I have to reconstruct the objects myself.

### Error Handling

I also practiced handling problems caused by invalid data, such as blank records.

### Debugging

Most importantly, I practiced debugging instead of immediately replacing my code with a completely different solution.

---

## 10. How I Used ChatGPT

I used ChatGPT as a **learning and debugging assistant**, not as the person writing the project for me.

I wrote the initial code myself.

Whenever I got stuck, I showed the code and explained what I was trying to accomplish. Instead of simply taking a finished solution, I focused on understanding:

* Why my code wasn't behaving as expected.
* What type of data I was actually working with.
* Why a file record wasn't an `Employee` object.
* Why iterating over `file.read()` gave me characters.
* Why the CSV caused an unpacking error.
* Why records were being duplicated.
* How aggregation and file handling could coexist.

The most useful part was understanding **why** something worked or failed.

I then applied those ideas back to my own code.

---

## Final Reflection

This wasn't a large project, but it was a useful practice because I wasn't trying to memorize syntax.

I started with a simple idea:

> A company has employees, and I want to save those employees to a file.

While implementing it, I encountered several problems that forced me to understand what was actually happening underneath the code.

The biggest lesson for me was that **objects in Python and data stored in a file are not the same thing**.

An `Employee` object exists in memory, while the CSV contains plain text. If I want to turn the stored text back into an object, I have to reconstruct it.

That made the connection between **OOP, Aggregation, and File Handling** much clearer to me.

I consider this project a piece of practice code that I built myself, with ChatGPT helping me understand and debug the places where I got stuck.
