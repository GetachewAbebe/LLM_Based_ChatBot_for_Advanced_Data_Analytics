import psycopg2
import csv

def load_subscription_data(conn):
    with open('table_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO SubscriptionTable (subscription_status, views, watch_time_hours, average_view_duration) VALUES (%s, %s, %s, %s)",
                (row[0], int(row[1]), float(row[2]), row[3])
            )
            conn.commit()
            cursor.close()

def load_chart_data(conn):
    with open('chart_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO SubscriptionChart (date, subscription_status, views) VALUES (%s, %s, %s)",
                (row[0], row[1], int(row[2]))
            )
            conn.commit()
            cursor.close()

def load_totals_data(conn):
    with open('totals.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO SubscriptionTotals (date, views) VALUES (%s, %s)",
                (row[0], int(row[1]))
            )
            conn.commit()
            cursor.close()

if __name__ == "__main__":
    try:
        conn = psycopg2.connect(
            dbname="youtube_analytics",
            user="daisy",
            password="password", # replace with evironement variable
            host="localhost",
            port="5432"
        )

        load_subscription_data(conn)
        load_chart_data(conn)
        load_totals_data(conn)

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
    finally:
        if conn is not None:
            conn.close()
# add more functions to load the rest of the tables for each cateory as per schema.sql