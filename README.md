# Assignment Test - Salary per Hour

![image](https://github.com/calvinnoval/assignment/assets/136886566/160749ca-a236-4324-8c08-81cfdab44f46)

Goal: Determine Salary per hour based on number of work for that branch each month

This repository contains the code and instructions for the Assignment Test that involves SQL processing using BigQuery and submitting a Python job using Dataproc.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Instructions](#instructions)

## Introduction
In this assignment, we will be performing SQL processing using Google BigQuery, a fully-managed, serverless data warehouse that enables super-fast SQL queries using the processing power of Google's infrastructure. We will also utilize Google Dataproc, a fast, easy-to-use, fully-managed cloud service for running Apache Spark and Apache Hadoop clusters, to submit a Python job for processing data.

## Prerequisites
To complete this assignment, you will need the following:
1. A Google Cloud Platform (GCP) account with access to BigQuery and Dataproc services.
2. Google Cloud SDK installed on your local machine to interact with GCP services.
3. Python installed on your local machine.
4. A sample `employees.csv` and `timesheets.csv` file that you want to process using SQL and Python.

## Instructions
Follow the steps below to complete the assignment:

1. **Setup Google Cloud Environment**
   - Ensure you have created a GCP account and set up your project.
   - Enable the BigQuery and Dataproc APIs in your GCP project.

2. **Create a BigQuery Dataset**
   - Use the BigQuery console or command-line tools to create a new dataset to store the processed data.

3. **Import Data into BigQuery**
   - Upload sample file given into BigQuery. You can use `main.py` for this task.

4. **Write SQL Queries**
   - Use BigQuery's SQL syntax to write queries that extract load transform your data into data warehouse.
   - Prepare table data warehouse with name `fact_detail_salary` to store daily snapshot <br />
    <br />
    <details><summary>DDL table</summary>  <br />
      CREATE TABLE `{project_id}.{dataset_id}.fact_detail_salary` <br />
      ( <br />
         year	INTEGER <br />
       , month	INTEGER	<br />			
       , branch_id	INTEGER	<br />			
       , salary_per_hour	FLOAT	<br />				
       , snapshot_date	DATE	<br />
      ) <br />
      PARTITION BY snapshot_date <br />
      CLUSTER BY branch_id, year, month
   </details> 

6. **Submit Python Job to Dataproc**
   - Write Python code to process the data further.
   - Save the Python script as `main.py` in the `assignment/` folder.

7. **Finalize and Submit**
   - Ensure your code is well-documented and any specific instructions are provided in the `README.md` file.

8. **Expected Result**
   - Expected result store to `fact_detail_salary.csv`
