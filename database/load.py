import os
import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port=15432
)
cur = conn.cursor()

data_dir = "/home/daisy/Desktop/tenx/week3/LLM_Based_ChatBot_for_Advanced_Data_Analytics/data"

# Iterate over CSV files in the directory
for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.endswith(".csv"):
            table_name = os.path.splitext(file)[0]  # Extract table name from file name
            file_path = os.path.join(root, file)  # Full path to CSV file

            copy_command = f"\copy {table_name} FROM '{file_path}' CSV HEADER;"

            print(copy_command)

            cur.execute(copy_command)
            conn.commit()

cur.close()
conn.close()
