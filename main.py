import os
import gc
import sys
import time
import pytz
import datetime
import csv

from google.cloud import bigquery

# declare time
tz = pytz.timezone("Asia/Jakarta")

today_date = (datetime.datetime.now()).astimezone(tz).strftime("%Y-%m-%d")

if len(sys.argv) > 1:
    today_date = sys.argv[1]

project_id = "{}"
dataset_id = "{}"
path = "/{}"
tables = ["employees", "timesheets"]

# BigQuery connection
os.environ["GOOGLE_CLOUD_PROJECT"] = "{}"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}" #configuration file

client = bigquery.Client(project=project_id)

def query_process(query):
    try:
        df = client.query(query).result()    
    except Exception as e:
        raise e
    return df

# Load file to Bigquery
def load_to_bq(filepath, table_id):
    job_config = bigquery.LoadJobConfig(
        field_delimiter=",",
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )
    with open(filepath, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file, table_id, job_config=job_config
        )  # Make an API request.
        load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows.".format(destination_table.num_rows))

# Save query into CSV
def save_csv(data, filepath):
    try:
        keys = data[0].keys()
        with open(filepath, "w", newline="") as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
    except Exception as e:
        print(e)
        raise Exception(f"Failed to write data to {filepath}")

# Write CSV to Local
def write_csv_to_local(table):
    query = f"""
    SELECT year
         , month
         , branch_id
         , salary_per_hour
    FROM `{project_id}.{dataset_id}.{table}`
    WHERE 1 = 1
        AND snapshot_date = '{today_date}';
    """
    
    data = query_process(query)
    records = [dict(row) for row in data]
    filepath = path +  "/" + f"{table}.csv"
    save_csv(records, filepath)

    print(f"saving result to >> {filepath} Done!")

def create_table(table):
    if table == 'employees':
        employees = f"""
        DROP TABLE IF EXISTS `{project_id}.{dataset_id}.{table}`;

        CREATE TABLE `{project_id}.{dataset_id}.{table}` 
        (
            employe_id INTEGER
          , branch_id INTEGER
          , salary INTEGER
          , join_date DATE
          , resign_date DATE
        )
        PARTITION BY joint_date
        CLUSTER BY employe_id, branch_id;
        """
        query_process(employees)
    else:    
        timesheets = f"""
        DROP TABLE IF EXISTS `{project_id}.{dataset_id}.{table}`;

        CREATE TABLE `{project_id}.{dataset_id}.{table}` 
        (
            timesheet_id INTEGER
          , employee_id INTEGER
          , date DATE
          , checkin TIME
          , checkout TIME
        )
        PARTITION BY date
        CLUSTER BY employee_id;
        """
        query_process(timesheets)

def transform_date(table):

    transform = f"""
    CREATE OR REPLACE TABLE `{project_id}.{dataset_id}.{table}_stg`

    PARTITION BY snapshot_date
    CLUSTER BY branch_id, year, month AS

    WITH timesheets AS
    (
      SELECT timesheet_id
           , employee_id
           , date
           , CASE
                WHEN checkin IS NULL AND last_row = 1
                    THEN LAST_VALUE(checkin IGNORE NULLS) OVER (PARTITION BY employee_id ORDER BY date)
                WHEN checkin IS NULL AND first_row <= 10
                    THEN LAST_VALUE(checkin IGNORE NULLS) OVER (PARTITION BY employee_id ORDER BY date DESC)
                WHEN checkin IS NULL
                    THEN LAST_VALUE(checkin IGNORE NULLS) OVER (PARTITION BY employee_id ORDER BY date)
                ELSE checkin
             END AS checkin
           , CASE
                WHEN checkout IS NULL AND last_row = 1
                    THEN LAST_VALUE(checkout IGNORE NULLS) OVER (PARTITION BY employee_id ORDER BY date)
                WHEN checkout IS NULL AND first_row <= 10
                    THEN LAST_VALUE(checkout IGNORE NULLS) OVER (PARTITION BY employee_id ORDER BY date DESC)
                WHEN checkout IS NULL 
                    THEN LAST_VALUE(checkout IGNORE NULLS) OVER (PARTITION BY employee_id ORDER BY date)
                ELSE checkout
             END AS checkout
      FROM
      (
        SELECT *
             , ROW_NUMBER () OVER (PARTITION BY employee_id ORDER BY timesheet_id) AS first_row
             , ROW_NUMBER () OVER (PARTITION BY employee_id ORDER BY timesheet_id DESC) AS last_row
        FROM `{project_id}.{dataset_id}.timesheets`
      )
    ), transform AS
    (
      SELECT EXTRACT(YEAR FROM date) AS year
           , EXTRACT(MONTH FROM date) AS month
           , employee_id
           , SUM(ABS(TIME_DIFF(checkout, checkin, HOUR))) AS work_hour
      FROM timesheets AS a
      GROUP BY 1, 2, 3
    )

    SELECT a.year
         , a.month
         , b.branch_id
         , SUM(b.salary) / SUM(a.work_hour) AS salary_per_hour
         , DATE('{today_date}') snapshot_date
    FROM transform AS a
    LEFT JOIN `{project_id}.{dataset_id}.employees` AS b ON a.employee_id = b.employe_id
    WHERE 1 = 1
    GROUP BY 1, 2, 3
    ;

    DELETE FROM `{project_id}.{dataset_id}.{table}`
    WHERE snapshot_date = DATE('{today_date}');

    INSERT INTO `{project_id}.{dataset_id}.{table}`
    SELECT *
    FROM `{project_id}.{dataset_id}.{table}_stg`;
    """
    query_process(transform)

def main(table):
    create_table(table)
    load_to_bq(f"{path}/{table}.csv", f"{project_id}.{dataset_id}.{table}")

if __name__ == '__main__':
    result = [main(table) for table in tables]
    transform_date('fact_detail_salary')
    write_csv_to_local('fact_detail_salary')

    del result
    gc.collect()
