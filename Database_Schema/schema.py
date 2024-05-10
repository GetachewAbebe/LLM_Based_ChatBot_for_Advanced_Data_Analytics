from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import pandas as pd
from dotenv import load_dotenv
import psycopg2

load_dotenv()

username = os.getenv("POSTGRES_USERNAME")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST")
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DATABASE")

# Add error checking or default values
if None in (username, password, host, port, database):
    print("Error: Some environment variables are missing.")
    sys.exit(1)

database_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

# Create an SQLAlchemy engine
engine = create_engine(database_url, echo=True)  # Set echo=True for debug logging

# Define the SQLAlchemy declarative base
Base = declarative_base()

# Define the MergedData class representing the table in the database
class MergedData(Base):
    __tablename__ = 'merged_data'

    # Define columns based on your data structure
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    cities = Column(String)
    city_name = Column(String)
    geography = Column(String)
    views = Column(Integer)
    watch_time_hours = Column(Float)
    average_view_duration = Column(String)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Specify the base folder
base_folder = '../YouTubeData'

# Get a list of all subfolders in the base folder
subfolders = [f.path for f in os.scandir(base_folder) if f.is_dir()]

# Iterate through each subfolder
for subfolder in subfolders:
    try:
        # Construct the file path for each CSV within the subfolder
        merged_data_path = os.path.join(subfolder, 'merged_data.csv')

        # Read the merged data from CSV
        merged_data = pd.read_csv(merged_data_path)

        # Convert the DataFrame to a list of dictionaries
        data_to_insert = merged_data.to_dict(orient='records')

        # Insert data into the database
        session.bulk_insert_mappings(MergedData, data_to_insert)

    except Exception as e:
        print(f"Error processing {subfolder}: {str(e)}")

# Commit the changes to the database
session.commit()

# Close the database session
session.close()