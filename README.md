# Employees_Judiciarydb
# Employee Database Management with SQLite and Python
This Python script demonstrates how to manage an employee database using SQLite. It creates a database named employees.db, establishes a connection, and performs these actions:
## Initialization:
Drops the existing employees table if it exists to start fresh.
Creates a new employees table with columns for ID, name, and job number.
## Data Insertion:
Adds twelve employees to the database with job numbers starting from 8200 which is the current number of employees in The Judiciary.
Each employee is given a unique ID, and their names are generated automatically.
## Data Display:
Retrieves all employees from the database after insertion.
Prints the details of each employee, including their ID, name, and job number.
## Closing Connection:
Closes the connection to the SQLite database once all operations are completed.
# Usage
1.Install SQLite3:
Ensure SQLite3 is installed on your system. If not, install it from the SQLite website or package manager.
2.Run the Script:
Execute the Python script employees.py in your preferred environment; command line or IDE.
3.View Output:
After execution, the script will display the details of all employees added to the database.
### Notes
Modify the initial_job_number variable to change the starting job number for employees.
Customize the script to suit your specific database schema and employee data requirements.