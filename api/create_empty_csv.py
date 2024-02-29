import csv
import sys

def create_empty_csv(user_id):
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Add header

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])
        create_empty_csv(user_id)
    else:
        print("Usage: python3 create_empty_csv.py <user_id>")
