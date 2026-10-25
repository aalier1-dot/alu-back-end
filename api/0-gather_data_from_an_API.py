#!/usr/bin/python3
"""Display an employee's completed TODO tasks from JSONPlaceholder."""

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
    """Print the completed TODO tasks for the employee ID argument."""
    if len(sys.argv) != 2:
        raise SystemExit("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        raise SystemExit("EMPLOYEE_ID must be an integer")

    user = fetch_json("{}/users/{}".format(API_URL, employee_id))
    query = urllib.parse.urlencode({"userId": employee_id})
    todos = fetch_json("{}/todos?{}".format(API_URL, query))

    completed_tasks = [
        task.get("title") for task in todos if task.get("completed")
    ]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed_tasks), len(todos)
        )
    )
    for title in completed_tasks:
        print("\t {}".format(title))


if __name__ == "__main__":
    main()
