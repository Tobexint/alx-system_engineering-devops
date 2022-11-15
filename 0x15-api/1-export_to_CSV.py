#!/usr/bin/python3
"""
Gather data from an API
Gets information from https://jsonplaceholder.typicode.com/todos/1
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    import csv

    if len(argv) > 1:
        args = argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'
        tasks = requests.get(url.format(args)).json()
        employee = requests.get(url[:-7].format(args)).json()
        file_name = '{}.csv'.format(args)
        to_file = []
        for i in range(len(tasks)):
            to_file.append(["{}".format(employee['id']),
                           "{}".format(employee['username']),
                            "{}".format(tasks[i]['completed']),
                            "{}".format(tasks[i]['title'])])
        with open(file_name, 'w') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerows(to_file)

        f.close()
