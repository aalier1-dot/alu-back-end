#!/usr/bin/python3
"""Export every employee's TODO list to a JSON file."""

import json
import urllib.request


API_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Fetch and decode a JSON response from the given URL."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def main():
    """Write all employees' TODO tasks to todo_all_employees.json."""
    users = fetch_json("{}/users".format(API_URL))
    todos = fetch_json("{}/todos".format(API_URL))
    usernames = {
        user.get("id"): user.get("username")
        for user in users
    }
    all_tasks = {}

    for task in todos:
        employee_id = task.get("userId")
        key = str(employee_id)
        if key not in all_tasks:
            all_tasks[key] = []
        all_tasks[key].append({
            "username": usernames.get(employee_id),
            "task": task.get("title"),
            "completed": task.get("completed"),
        })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    main()
