# EHR Data Transfer to MySQL

This Python script automates the process of transferring patient medical data from an EHR (Electronic Health Records) file in CSV format to a MySQL database. The script includes a manual review step where the user can verify each record before it is inserted into the database.

## Features

- Reads EHR data from a CSV file
- Prompts the user to review and authorize each record before updating the database
- Records the authorizing person's name for each row
- Inserts the data, today's date, and the authorizing person's name into the database

## Requirements

- Python 3.x
- `mysql-connector-python` library
- `pandas` library

## Installation

1. Install Python 3.x: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install the required libraries by running these commands in your terminal or command prompt:

```bash
pip install mysql-connector-python
pip install pandas
```

## Configuration

1. Replace the placeholders in the `db_config` dictionary with your actual MySQL database credentials.
2. Replace the `ehr_file_path` variable with the path to your EHR file in CSV format.
3. Replace `your_table_name` with the name of the table you're using in your RedCap database.

## Usage

1. Save the script as `ehr_to_mysql.py`.
2. Run the script using the command `python ehr_to_mysql.py`.

The script will read the EHR data from the CSV file, prompt you to review and authorize each row, and insert the data into the specified MySQL table.

