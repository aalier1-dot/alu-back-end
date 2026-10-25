# API

These scripts use the JSONPlaceholder REST API to retrieve employee and TODO
data.

## Requirements

- Python 3
- Network access to `https://jsonplaceholder.typicode.com`

## Usage

Display the completed TODO tasks for an employee:

```sh
python3 0-gather_data_from_an_API.py EMPLOYEE_ID
```

Export all TODO tasks for one employee to CSV:

```sh
python3 1-export_to_CSV.py EMPLOYEE_ID
```

Export all TODO tasks for one employee to JSON:

```sh
python3 2-export_to_JSON.py EMPLOYEE_ID
```

Export all employees' TODO tasks to JSON:

```sh
python3 3-dictionary_of_list_of_dictionaries.py
```

The CSV and per-employee JSON scripts create a file named after the employee
ID in the current directory. The all-employees script creates
`todo_all_employees.json`.

