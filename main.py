import pyodbc

# Define the path to your .accdb file
db_path = r"C:\Hackaton_October\main_data.accdb"


# Create a connection string using the ODBC driver for Access
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=' + db_path + ';'
)

# Connect to the Access database
conn = pyodbc.connect(conn_str)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# SQL query to select the ОКПД2 column from the table MTR
query = "SELECT ОКПД2 FROM MTR"

# Initialize an empty list to store the OKPD2 values
okpd2_data = []

# Fetch rows in batches to handle large data efficiently
batch_size = 10000  # Adjust this value based on memory constraints
cursor.execute(query)

# Fetch data in batches and append to the list
while True:
    rows = cursor.fetchmany(batch_size)
    if not rows:
        break
    okpd2_data.extend([row[0] for row in rows])

# Close the connection
cursor.close()
conn.close()

# At this point, okpd2_data contains all the values from the ОКПД2 column
print(f"Retrieved {len(okpd2_data)} rows from OKPD2.")