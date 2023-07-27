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
4. A sample dataset that you want to process using SQL and Python.

## Instructions
Follow the steps below to complete the assignment:

1. **Setup Google Cloud Environment**
   - Ensure you have created a GCP account and set up your project.
   - Enable the BigQuery and Dataproc APIs in your GCP project.

2. **Create a BigQuery Dataset**
   - Use the BigQuery console or command-line tools to create a new dataset to store the processed data.

3. **Import Data into BigQuery**
   - Upload or import your sample dataset into BigQuery. You can use the console, command-line tools, or Python libraries for this task.

4. **Write SQL Queries**
   - Use BigQuery's SQL syntax to write queries that process and analyze your data. Save these queries as `.py` files in the `assignment/` folder.

5. **Submit Python Job to Dataproc**
   - Write Python code to process the data further.
   - Save the Python script as `main.py` in the `assignment/` folder.

6. **Finalize and Submit**
   - Ensure your code is well-documented and any specific instructions are provided in the `README.md` file.

7. **Expected Result**
   - Expected result store to `fact_detail_salary.csv`
