#!/usr/bin/python3
"""
Gather data from an API
Gets information from https://jsonplaceholder.typicode.com/todos/1
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    import json

    if len(argv) > 1:
        args = argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'
        tasks = requests.get(url.format(args)).json()
        employee = requests.get(url[:-7].format(args)).json()
        file_name = '{}.json'.format(args)
        data = []
        for t in tasks:
            data.append({
                "task": t['title'],
                "completed": t['completed'],
                "username": employee['username']
            })
        to_file = {args: data}
        with open(file_name, 'w') as f:
            f.write(json.dumps(to_file))

        f.close()
