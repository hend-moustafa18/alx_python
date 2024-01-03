# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import MySQLdb

def filter_states(username, password, database_name):
    """Lists states with names starting with 'N' from the specified database."""

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()

# Example usage:
if __name__ == "__main__":
    filter_states("root", "root", "hbtn_0e_0_usa")