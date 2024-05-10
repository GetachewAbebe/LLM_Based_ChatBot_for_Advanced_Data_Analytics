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

directory = "/home/daisy/Desktop/tenx/week3/LLM_Based_ChatBot_for_Advanced_Data_Analytics/data"

# Iterate over CSV files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Construct full file path
        file_path = os.path.join(directory, filename)
        
        table_name = os.path.splitext(filename)[0]

        with open(file_path, 'r') as f:
            next(f)

            # Copy data from CSV file to PostgreSQL table
            cur.copy_from(f, table_name, sep=',', columns=None)

            conn.commit()

cur.close()
conn.close()
