# Logic Salary per Hour

![image](https://github.com/calvinnoval/assignment/assets/136886566/160749ca-a236-4324-8c08-81cfdab44f46)

Goal: Determine Salary per hour based on number of work for that branch each month


a) SQL

- Create a schema and load each CSV file to employees and timesheets tables.
- Write an SQL script that reads from employees and timesheets tables, transforms, and loads the destination table.
- The script is expected to run daily in full-snapshot mode, meaning that it will read the whole table and then overwrite the result in the destination table. Note that you don’t have to implement the scheduler, just the script that will be run by the scheduler.

b) Python

- Write a Python or Java code that reads from CSV files, transforms, and loads to the destination table.
- The code is expected to run daily in incremental mode, meaning that each day it will only read the new data and then appends the result to the destination table. Note that you don’t have to implement the scheduler, just the script that will be run by the scheduler.
