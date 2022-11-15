#!/usr/bin/python3
"""
Gather data from an API
Gets information from https://jsonplaceholder.typicode.com/todos/1
"""


def get_done_tasks(task):
    """ Gets all done tasks"""
    tasks_finished = []
    tasks_unfinished = []
    list_finished = []
    for t in range(len(task)):
        tasks_finished.append(task[t]['completed'] is True)
        if task[t]['completed'] is False:
            tasks_unfinished.append(task[t]['completed'] is False)
        else:
            list_finished.append(task[t]['title'])
    return tasks_finished, tasks_unfinished, list_finished


if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) > 1:
        args = argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'
        tasks = requests.get(url.format(args)).json()
        employee = requests.get(url[:-7].format(args)).json()
        data = get_done_tasks(tasks)
        print('Employee {} is done with tasks({}/{}):'.format(
            employee['name'],
            len(tasks) - len(data[1]),
            len(tasks)))
        for t in data[2]:
            print("\t {}".format(t))
        # print(employee)
