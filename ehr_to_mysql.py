import pandas as pd
import mysql.connector
from mysql.connector import Error
from datetime import date

# Database connection configuration
db_config = {
    "host": "your_host",
    "user": "your_user",
    "password": "your_password",
    "database": "RedCap",
}

# Function to establish a connection to the MySQL database
def create_db_connection(config):
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None



# Function to close the database connection
def close_db_connection(connection):
    if connection:
        connection.close()


# Function to insert data into the database
def insert_data(connection, row, authorized_by):
    cursor = connection.cursor()
    insert_query = """
        INSERT INTO your_table_name (
            patient_name,
            DOB,
            Research_ID_number,
            Medical_Record_Number,
            Diagnosis,
            Date_of_surgery,
            Gleason_score,
            prostate_specific_antigen_score,
            import_date,
            authorized_by
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        cursor.execute(insert_query, (
            row["patient_name"],
            row["DOB"],
            row["Research_ID_number"],
            row["Medical_Record_Number"],
            row["Diagnosis"],
            row["Date_of_surgery"],
            row["Gleason_score"],
            row["prostate_specific_antigen_score"],
            date.today(),
            authorized_by
        ))
        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting data into the database: {e}")

# Function to display a row and prompt the user for authorization
def review_and_authorize(row):
    print("\nReview the following data:")
    print(row)

    authorized = input("\nAuthorize this update? (yes/no): ")
    if authorized.lower() == "yes":
        authorized_by = input("Enter the name of the authorizing person: ")
        return authorized_by
    else:
        return None

# Main function to read the EHR file and insert data into the MySQL database
def main():
    ehr_file_path = "path/to/your/ehr_file.csv"
    ehr_data = pd.read_csv(ehr_file_path)

    connection = create_db_connection(db_config)

    if connection:
        for index, row in ehr_data.iterrows():
            authorized_by = review_and_authorize(row)
            if authorized_by:
                insert_data(connection, row, authorized_by)

        close_db_connection(connection)
        print("\nData transfer complete.")
    else:
        print("Could not transfer data due to a database connection issue.")


if __name__ == "__main__":
    main()
