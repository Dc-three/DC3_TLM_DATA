import pandas as pd
import mysql.connector
import numpy as np
from datetime import datetime
csv_file_path1 = './final_ATTRIBUTE_DATA.csv'


data1 = pd.read_csv(csv_file_path1)


if not data1.empty:
        data1.replace({np.nan: None, 'nan': None}, inplace=True)

else:
        print("The DataFrame is empty.")
        exit(1)


# Define a function to preprocess datetime values
def preprocess_datetime(value):
    try:
        # Attempt to parse and reformat the datetime value
        # Adjust the format according to your needs
        
        
        if pd.isna(value):
            return 0 # Handle NaN values
        # Attempt to parse and reformat the datetime value
        datetime_value = pd.to_datetime(value, errors='coerce')
        
        # If the conversion to datetime is successful, format it as 'HH:MM:SS'
        if not pd.isnull(datetime_value):
            return datetime_value.strftime('%H:%M:%S')
        
        # If the conversion fails (result is NaT), return 0
        return 0
    
    except Exception as e:
        # In case of any other errors, return 0
        return 0
# Apply preprocessing to the specific column containing datetime values
# Replace 'your_datetime_column' with the actual column name
if 'your_datetime_column' in data1.columns:
    data1['your_datetime_column'] = data1['your_datetime_column'].apply(preprocess_datetime)


# Database connection details
db_config = {
    'user': 'admin2',
    'password': 'common104',
    'host': 'qsdatabase-instance-1.c9a808e8em1p.us-east-2.rds.amazonaws.com',
    'database': 'dc3',
    'raise_on_warnings': True
}

# Connect to the MySQL database
cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()





# Insert data into the MySQL table row by row
table_name = 'AttributeData'  # Your table name  

for _, row in data1.iterrows():
    # Construct the INSERT INTO query
    columns = ', '.join(row.index)
    placeholders = ', '.join(['%s'] * len(row))
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Execute the query with the row data
    try:
        cursor.execute(sql, tuple(row))
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        # Optionally log the row or handle the error as needed
cnx.commit()




# Close the cursor and connection
cursor.close()
cnx.close()
