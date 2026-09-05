# Employee Management System

A Python practice project demonstrating **Object-Oriented Programming, Aggregation, File Handling, CSV parsing, Type Validation, and Object Reconstruction**.

---

# 1. Program Overview

The program models a simple company and its employees.

The program has two main classes:

```text
┌─────────────────────────┐
│        Employee         │
├─────────────────────────┤
│ name                    │
│ designation             │
│ salary                  │
├─────────────────────────┤
│ display_employee_data() │
└─────────────────────────┘
             ▲
             │
             │ has
             │
┌─────────────────────────┐
│         Company         │
├─────────────────────────┤
│ company_name            │
│ employees[]             │
├─────────────────────────┤
│ add_employee()          │
│ show_employees()        │
└─────────────────────────┘
             │
             │
             ▼
       ┌───────────┐
       │ Lists.csv │
       └───────────┘
```

The program follows this general structure:

```text
Employee Class
      │
      │ creates
      ▼
Employee Objects
      │
      │ added to
      ▼
Company Object
      │
      ├──────────────► employees[]
      │
      └──────────────► Lists.csv
                              │
                              │ read
                              ▼
                       CSV Records
                              │
                              │ reconstruct
                              ▼
                       Employee Objects
```

---

# 2. Core Architecture

The program has three main responsibilities:

### Employee

Responsible for representing an individual employee.

```text
Employee
├── name
├── designation
├── salary
└── display_employee_data()
```

### Company

Responsible for managing a collection of employees.

```text
Company
├── company_name
├── employees[]
├── add_employee()
└── show_employees()
```

### CSV File

Responsible for persistent storage.

```text
Lists.csv

Name,Designation,Salary
Alice,Manager,80000.0
Bob,Developer,60000.0
Vijay,System Architect,75980.5
```

The Python objects exist in memory while the program runs. The CSV stores their data so it can be retrieved later.

---

# 3. `Employee` Class

```python
class Employee:
```

This defines a class named `Employee`.

A class is a blueprint used to create objects.

The class defines both:

* **State** → employee attributes
* **Behavior** → employee methods

An object created from this class represents one actual employee.

---

## 3.1 Constructor

```python
def __init__(self, name, designation, salary):
```

`__init__()` is automatically executed when an `Employee` object is created.

For example:

```python
employee1 = Employee("Alice", "Manager", 80000.0)
```

Python creates a new object and then calls:

```python
__init__(employee1, "Alice", "Manager", 80000.0)
```

The `self` parameter refers to the newly created object.

---

## 3.2 Instance Attributes

```python
self.name = name
self.designation = designation
self.salary = salary
```

These create **instance attributes**.

For:

```python
employee1 = Employee("Alice", "Manager", 80000.0)
```

the object internally has values equivalent to:

```text
employee1
│
├── name → "Alice"
├── designation → "Manager"
└── salary → 80000.0
```

`self.name` belongs to the object.

`name` is the local parameter received by `__init__()`.

So:

```python
self.name = name
```

means:

> Store the value received through `name` inside this object's `name` attribute.

---

# 4. Salary Validation

```python
if not isinstance(self.salary, (float)):
    raise ValueError("Salary must be float")
```

This applies **type validation**.

`isinstance()` checks whether a value belongs to a particular type.

For example:

```python
isinstance(80000.0, float)
```

returns:

```text
True
```

Therefore:

```python
not isinstance(self.salary, float)
```

is `False`, so no exception is raised.

If someone tries:

```python
Employee("Alice", "Manager", "80000")
```

the salary is a string.

The condition becomes true and:

```python
raise ValueError("Salary must be float")
```

raises an exception.

### Logic

```text
Salary received
      │
      ▼
Is salary a float?
   /          \
 Yes           No
  │             │
  ▼             ▼
Continue     Raise ValueError
```

This prevents an invalid salary type from being accepted by the class.

---

# 5. Employee Display Method

```python
def display_employee_data(self):
    return f"Name: {self.name} | Designation: {self.designation} | Salary: {self.salary} BDT"
```

This is an **instance method**.

It operates on the specific object represented by `self`.

For:

```python
employee1.display_employee_data()
```

`self` refers to `employee1`.

Therefore:

```python
self.name
```

effectively accesses:

```python
employee1.name
```

The method returns a formatted string rather than directly printing it.

That allows the caller to decide what to do with the returned value:

```python
print(employee1.display_employee_data())
```

---

# 6. `Company` Class

```python
class Company:
```

This class represents a company.

A company contains:

```text
Company
├── company_name
└── employees
```

It also provides operations for managing those employees.

---

# 7. Company Constructor

```python
def __init__(self, company_Name):
    self.company_name = company_Name
    self.employees = []
```

When:

```python
company = Company("XYZ")
```

is executed, Python creates a company object.

Its initial state becomes:

```text
company
│
├── company_name → "XYZ"
└── employees → []
```

The empty list is important because it will later contain `Employee` objects.

---

# 8. Aggregation

The relationship between `Company` and `Employee` is represented through:

```python
self.employees = []
```

and:

```python
self.employees.append(employee)
```

This demonstrates **Aggregation**.

Aggregation represents a relationship where one object contains or manages other objects, while those objects can exist independently.

In this project:

```text
             Company
                │
                │ has
                ▼
          employees[]
           /    |    \
          /     |     \
         ▼      ▼      ▼
    Employee Employee Employee
```

The employees are created separately:

```python
employee1 = Employee(...)
employee2 = Employee(...)
employee3 = Employee(...)
```

Then they can be associated with the company.

The company does not need to create the employees itself.

---

# 9. `add_employee()`

```python
def add_employee(self, employee):
```

This method accepts an `Employee` object.

For example:

```python
company.add_employee(employee1)
```

Inside the method:

```python
self.employees.append(employee)
```

adds the object to the company's employee list.

Before:

```text
employees → []
```

After:

```text
employees → [employee1]
```

After adding all three:

```text
employees
   │
   ├── employee1
   ├── employee2
   └── employee3
```

The list stores **references to objects**, not copies of their data.

---

# 10. Writing Employee Data to the File

The second responsibility of `add_employee()` is persistent storage:

```python
with open("Lists.csv", 'a') as file:
```

`open()` opens the file.

The mode:

```python
'a'
```

means **append mode**.

Existing content is preserved and new content is added at the end.

The `with` statement acts as a context manager and ensures that the file is properly closed after the block finishes.

The structure is:

```text
Open file
    ↓
Execute operations
    ↓
Leave `with` block
    ↓
File automatically closed
```

---

# 11. Converting Employee Data Into CSV

```python
file.write(
    f"{employee.name},{employee.designation},{employee.salary}\n"
)
```

The object contains structured Python data:

```text
name = "Alice"
designation = "Manager"
salary = 80000.0
```

The code converts those values into a CSV-formatted string:

```text
Alice,Manager,80000.0
```

`\n` adds a newline so the next employee will be written on a separate line.

Therefore:

```text
Python Object
     ↓
Extract attributes
     ↓
Create CSV string
     ↓
Write to file
```

---

# 12. `show_employees()`

```python
def show_employees(self):
```

This method retrieves employee information from the CSV file.

It starts by displaying the company name:

```python
print(f"{self.company_name}'s Employees\n")
```

Then the file is opened in read mode:

```python
with open("Lists.csv", 'r') as file:
```

`'r'` means **read mode**.

No data is written or modified.

---

# 13. Reading the File Line by Line

```python
for record in file:
```

A file object is iterable.

Instead of loading the entire file into memory, Python reads it one line at a time.

For example:

```text
Alice,Manager,80000.0
Bob,Developer,60000.0
Vijay,System Architect,75980.5
```

is processed approximately as:

```text
Iteration 1 → "Alice,Manager,80000.0\n"
Iteration 2 → "Bob,Developer,60000.0\n"
Iteration 3 → "Vijay,System Architect,75980.5\n"
```

This is why using:

```python
for record in file:
```

is appropriate for processing individual CSV records.

---

# 14. Removing Whitespace

```python
record = record.strip()
```

A line read from the file may contain a newline character:

```text
"Alice,Manager,80000.0\n"
```

`.strip()` removes surrounding whitespace.

It becomes:

```text
"Alice,Manager,80000.0"
```

This makes the record easier to process.

---

# 15. Skipping Empty Lines

```python
if not record:
    continue
```

After `.strip()`, an empty line becomes:

```python
""
```

An empty string evaluates to `False`.

Therefore:

```python
if not record:
```

means:

> If the record contains no data, skip it.

`continue` immediately moves the loop to the next record.

This prevents empty lines from reaching the CSV parsing logic.

---

# 16. Splitting the CSV Data

```python
name, designation, salary = record.split(',')
```

Suppose:

```python
record = "Alice,Manager,80000.0"
```

Then:

```python
record.split(',')
```

returns:

```python
["Alice", "Manager", "80000.0"]
```

Python then performs **sequence unpacking**:

```text
name        ← "Alice"
designation ← "Manager"
salary      ← "80000.0"
```

This is why each valid CSV record must contain exactly three fields.

---

# 17. Converting the Salary Back to a Float

When data is read from a text file, it is read as text.

Therefore:

```python
salary
```

is initially:

```python
"80000.0"
```

not:

```python
80000.0
```

The code therefore uses:

```python
float(salary)
```

to convert the string into a floating-point number.

```text
"80000.0"
     ↓
   float()
     ↓
80000.0
```

This is necessary because the `Employee` constructor validates that salary must be a float.

---

# 18. Reconstructing an Employee Object

```python
employee = Employee(name, designation, float(salary))
```

This is the bridge between **File Handling and OOP**.

The CSV contains only text:

```text
Alice,Manager,80000.0
```

The program converts that text back into structured Python data and creates a new `Employee` object.

```text
CSV Record
    │
    ▼
split(',')
    │
    ▼
name / designation / salary
    │
    ▼
float(salary)
    │
    ▼
Employee(...)
    │
    ▼
New Employee Object
```

This process can be called **object reconstruction**.

The object originally written to the file is not literally stored inside the CSV. Only its data is stored.

A new object is created when the data is read.

---

# 19. Displaying the Reconstructed Object

```python
print(employee.display_employee_data())
```

At this point, `employee` is a normal `Employee` object.

Therefore it has access to the method:

```python
display_employee_data()
```

The method returns a formatted string, and `print()` displays that string.

---

# 20. Creating Employee Objects

```python
employee1 = Employee("Alice", "Manager", 80000.0)
employee2 = Employee("Bob", "Developer", 60000.0)
employee3 = Employee("Vijay", "System Architect", 75980.5)
```

Each line creates a separate `Employee` instance.

The resulting structure is conceptually:

```text
employee1 → Employee
             ├── Alice
             ├── Manager
             └── 80000.0

employee2 → Employee
             ├── Bob
             ├── Developer
             └── 60000.0

employee3 → Employee
             ├── Vijay
             ├── System Architect
             └── 75980.5
```

Each object maintains its own state.

---

# 21. Creating the Company

```python
company = Company("XYZ")
```

This creates a `Company` object:

```text
company
│
├── company_name → "XYZ"
└── employees → []
```

Employees can then be associated with it using:

```python
company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)
```

---

# 22. Why `add_employee()` Is Currently Commented

In the current code:

```python
#company.add_employee(employee1)
#company.add_employee(employee2)
#company.add_employee(employee3)
```

these lines are commented out.

Therefore, during this particular execution:

* No new employees are added to `company.employees`.
* No new records are appended to `Lists.csv`.

However:

```python
company.show_employees()
```

still reads the existing records from `Lists.csv`.

This means the program can demonstrate the file-reading and object-reconstruction process independently from the file-writing process.

---

# 23. Complete Execution Flow

When employee records are being added:

```text
1. Create Employee
        ↓
2. Create Company
        ↓
3. company.add_employee(employee)
        ↓
4. Add Employee reference to employees[]
        ↓
5. Extract employee attributes
        ↓
6. Convert attributes to CSV text
        ↓
7. Append text to Lists.csv
```

When employee records are being displayed:

```text
1. Open Lists.csv
        ↓
2. Read one record
        ↓
3. strip()
        ↓
4. Check for empty record
        ↓
5. split(',')
        ↓
6. Extract name, designation, salary
        ↓
7. Convert salary to float
        ↓
8. Create Employee object
        ↓
9. Call display_employee_data()
        ↓
10. Print result
```

---

# 24. Data Flow

The project has two important data flows.

## Saving

```text
Employee Object
      │
      ├── name
      ├── designation
      └── salary
             │
             ▼
        CSV String
             │
             ▼
         Lists.csv
```

## Loading

```text
Lists.csv
    │
    ▼
CSV String
    │
    ▼
split(',')
    │
    ▼
Individual Values
    │
    ▼
Type Conversion
    │
    ▼
Employee(...)
    │
    ▼
Employee Object
```

So the overall process is:

```text
             SAVE
Object ─────────────────► File
  ▲                         │
  │                         │
  │                         ▼
  └────────────────────── Data
             LOAD
```

---

# 25. Memory vs Persistent Storage

A major distinction in this program is between **objects in memory** and **data stored in a file**.

### Python Memory

An employee object contains:

```text
Data
+
Methods / Behavior
```

For example:

```text
Employee Object
├── name
├── designation
├── salary
└── display_employee_data()
```

### CSV File

The CSV only contains:

```text
Alice,Manager,80000.0
```

It does not contain:

* The `Employee` class
* Python methods
* Object references
* Object behavior

Therefore, when reading the file, the program must recreate an `Employee` object.

---

# 26. Important Python Concepts Used

| Code                              | Concept                  |
| --------------------------------- | ------------------------ |
| `class Employee`                  | Class definition         |
| `Employee(...)`                   | Object instantiation     |
| `__init__()`                      | Object initialization    |
| `self`                            | Current object reference |
| `self.name`                       | Instance attribute       |
| `def display_employee_data()`     | Instance method          |
| `isinstance()`                    | Type checking            |
| `raise ValueError()`              | Raising an exception     |
| `class Company`                   | OOP                      |
| `self.employees = []`             | Object collection        |
| `.append()`                       | List operation           |
| `Company → Employee`              | Aggregation              |
| `open(..., 'a')`                  | File append mode         |
| `open(..., 'r')`                  | File read mode           |
| `with open()`                     | Context manager          |
| `file.write()`                    | File output              |
| `for record in file`              | File iteration           |
| `.strip()`                        | Whitespace removal       |
| `.split(',')`                     | CSV parsing              |
| `name, designation, salary = ...` | Sequence unpacking       |
| `float(salary)`                   | Type conversion          |
| `continue`                        | Loop control             |
| `try/except`                      | Exception handling       |
| `f"..."`                          | f-string formatting      |

---

# 27. Key Concepts to Remember

### Class

A blueprint for creating objects.

```python
class Employee:
```

### Object

An instance created from a class.

```python
employee1 = Employee(...)
```

### Encapsulation

The employee's data and behavior are grouped together inside the `Employee` class.

```text
Employee
├── Data
└── Behavior
```

### Aggregation

A `Company` maintains references to `Employee` objects.

```python
self.employees.append(employee)
```

### File Handling

Employee data is persisted outside the program using a CSV file.

```python
open("Lists.csv", 'a')
```

### Parsing

CSV text is separated into individual fields.

```python
record.split(',')
```

### Type Conversion

Text from the CSV is converted back into the required Python type.

```python
float(salary)
```

### Object Reconstruction

Stored data is used to create a new Python object.

```python
Employee(name, designation, float(salary))
```

---

# 28. Program in One Diagram

```text
                         ┌───────────────┐
                         │    Company    │
                         ├───────────────┤
                         │ company_name  │
                         │ employees[]   │
                         └───────┬───────┘
                                 │
                              Aggregation
                                 │
               ┌─────────────────┼─────────────────┐
               │                 │                 │
               ▼                 ▼                 ▼
          Employee 1        Employee 2        Employee 3
               │                 │                 │
               └─────────────────┼─────────────────┘
                                 │
                           add_employee()
                                 │
                                 ▼
                         ┌───────────────┐
                         │   Lists.csv   │
                         ├───────────────┤
                         │ Alice,...     │
                         │ Bob,...       │
                         │ Vijay,...     │
                         └───────┬───────┘
                                 │
                           show_employees()
                                 │
                                 ▼
                          Read CSV records
                                 │
                                 ▼
                           Parse each row
                                 │
                                 ▼
                          Convert salary
                                 │
                                 ▼
                      Reconstruct Employee
                                 │
                                 ▼
                       Display employee data
```

---

# 29. Final Technical Summary

This project demonstrates a simple cycle of:

```text
CREATE
  ↓
STORE
  ↓
READ
  ↓
PARSE
  ↓
RECONSTRUCT
  ↓
DISPLAY
```

The `Employee` class defines the individual object's structure and behavior.

The `Company` class demonstrates aggregation by maintaining a collection of employee objects.

The CSV file provides persistent storage for employee data.

When saving, an `Employee` object is converted into text.

When loading, that text is parsed and converted back into a newly created `Employee` object.

The most important conceptual relationship is therefore:

```text
Python Object
      ↕
  Data Conversion
      ↕
Persistent CSV Data
```

This is the core logic connecting **Object-Oriented Programming, Aggregation, and File Handling** in this project.
