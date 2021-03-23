from collections import deque
import requests
from .environment import Environment

prioritized_q = deque()    # This may be implemented by a (No)SQL database


def enqueue(data):
    uid = data['user_id']
    x = data['x']

    # Function _get)insertion_index_ may be implemented using various algorithms
    insertion_index = get_insertion_index(uid)
    prioritized_q.insert(insertion_index, (uid, x))
    return insertion_index


def call_service():
    while Environment.service_status == 'running':
        if prioritized_q:
            req = prioritized_q.popleft()
            res = requests.post('http://127.0.0.1:5001/limited/call',
                                json={"user_id": req[0], "x": req[1]})
            print("Request --> uid = " + str(req[0]) + " , X = " + str(req[1]) + " " + res.json()['message'] + "; " + str(len(prioritized_q)) + " remained")
    print('----------------------------------')
    if Environment.service_status == 'to stop':
        Environment.service_status == 'stopped'


def get_insertion_index(uid):
    uids = set([rec[0] for rec in prioritized_q])
    if uid not in uids:
        return len(uids)
    else:
        return len(prioritized_q)
