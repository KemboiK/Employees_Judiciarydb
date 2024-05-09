import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()

# Drop the existing employees table if it exists
cursor.execute("DROP TABLE IF EXISTS employees")

# Create a table for employees if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                (id INTEGER PRIMARY KEY, name TEXT, job_number INTEGER)''')

# Add twelve employees to the database with job numbers starting from 8200
initial_job_number = 8200
for i in range(1, 13):
    employee_name = f"Employee {i}"
    job_number = initial_job_number + i - 1  # Assign job numbers sequentially
    cursor.execute("INSERT INTO employees (name, job_number) VALUES (?, ?)", (employee_name, job_number))

# Commit changes to the database
conn.commit()

# Display all employees in the database
cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()
for employee in employees:
    print(employee)

# Close connection to the database
conn.close()
