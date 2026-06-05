import sqlite3
try:
    # Created a Student Database
    with sqlite3.connect("Students.db") as pointer : #Connected to the Database
        cursor = pointer.cursor() # Interacts with the DB

    # Query to Create a table
    create_Student_Data_Table = '''
        CREATE TABLE IF NOT EXISTS Students(
            Name TEXT NOT NULL,
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Semester_Completed INTEGER NOT NULL,
            CGPA REAL NOT NULL
        );
    '''
    cursor.execute(create_Student_Data_Table) #Build & Run the table
    # To Insert Data into the DB
    insert_Student_Data = '''
        INSERT INTO Students(Name, ID, Semester_Completed, CGPA)
        VALUES(:Name, :ID, :Semester_Completed, :CGPA);
    '''
    # Created Input system to insert Data
    #Created a while loop for recording multiple records
    while True:
        print(" Student Details Entry  ")

        name = input("Name: ").strip()
        if name.lower() == "exit":
            break
        id = input("ID: ")
        if id.lower() == "exit":
            break
        semester = input("Semester Completed: ").strip()
        if semester.lower() == "exit":
            break
        CGPA = input("CGPA: ")
        if CGPA.lower() == "exit":
            break
        
        # Binding inputs to a dictionary
        try: # To tackle Error
            multiple_records = {
                "Name": name,
                "ID": int(id),
                "Semester_Completed": int(semester),
                "CGPA": float(CGPA)
            }
            pointer.execute(insert_Student_Data, multiple_records)
        except ValueError:
                print("\n❌ Error: ID and Semester must be integers, and CGPA must be a decimal number. Please try again this record.\n")
                continue
    pointer.commit() # Commits changes

    print("Data Saved!")

except Exception as error:
    print(f"Error Occured:\n{error}")