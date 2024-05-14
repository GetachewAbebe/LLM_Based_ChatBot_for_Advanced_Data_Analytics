import asyncpg
import os

async def connect_to_db():
    conn = await asyncpg.connect(user='postgres', password='postgres',
                                 database='postgres', host='localhost')
    return conn

async def store_data(conn, directory):
    try:
        cur = await conn.cursor()
        # Get existing table names from the database
        existing_tables = await conn.fetch("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        existing_tables = {table['table_name'] for table in existing_tables}

        # Path to the directory containing CSV files
        csv_files = [filename for filename in os.listdir(directory) if filename.endswith('.csv')]
        
        # Load data from CSV files into the database
        for filename in csv_files:
            table_name = os.path.splitext(filename)[0]
            
            # Check if the table already exists in the database
            if table_name in existing_tables:
                print(f"Table '{table_name}' already exists. Skipping data loading.")
                continue
            
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as f:
                await cur.copy_from(f, table_name, sep=',', columns=None)
        
        await conn.commit()
    except asyncpg.exceptions.PostgresError as e:
        print(f"Error loading data from CSV: {e}")
