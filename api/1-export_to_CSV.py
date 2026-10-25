#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""

import csv
import json
import sys
import urllib.parse
import urllib.request


API_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Fetch and decode a JSON response from the given URL."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Write all TODO tasks for the employee ID argument to a CSV file."""
    if len(sys.argv) != 2:
        raise SystemExit("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        raise SystemExit("EMPLOYEE_ID must be an integer")

    user = fetch_json("{}/users/{}".format(API_URL, employee_id))
    query = urllib.parse.urlencode({"userId": employee_id})
    todos = fetch_json("{}/todos?{}".format(API_URL, query))

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                user.get("username"),
                task.get("completed"),
                task.get("title"),
            ])


if __name__ == "__main__":
    main()
