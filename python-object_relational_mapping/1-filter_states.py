#!/usr/bin/python3
import MySQLdb
import sys

def filter_states(username, password, database):
    try:
        # Connect to the MySQL server
        connection = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
        cursor = connection.cursor()

        # Select states starting with 'N' from the states table
        cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        results = cursor.fetchall()

        # Display the results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        if connection:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    filter_states(username, password, database)