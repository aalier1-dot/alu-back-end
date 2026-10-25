#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""

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
    """Write all TODO tasks for the employee ID argument to a JSON file."""
    if len(sys.argv) != 2:
        raise SystemExit("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        raise SystemExit("EMPLOYEE_ID must be an integer")

    user = fetch_json("{}/users/{}".format(API_URL, employee_id))
    query = urllib.parse.urlencode({"userId": employee_id})
    todos = fetch_json("{}/todos?{}".format(API_URL, query))
    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username"),
        }
        for task in todos
    ]

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)


if __name__ == "__main__":
    main()
