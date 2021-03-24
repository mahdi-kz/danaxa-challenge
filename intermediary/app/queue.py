from collections import deque
import requests
from .environment import Environment

prioritized_q = deque()    # This may be implemented by a (No)SQL database


def enqueue(data):
    uid = data['user_id']
    x = data['x']

    # Function _get)insertion_index_ may be implemented using various algorithms
    insertion_index = get_insertion_index_1(uid)
    prioritized_q.insert(insertion_index, (uid, x))
    return insertion_index


def call_service():
    while Environment.service_status == 'running':
        if prioritized_q:
            req = prioritized_q.popleft()
            res = requests.post(Environment.limited_f_url,
                                json={"user_id": req[0], "x": req[1]})
            print("Request --> uid = " + str(req[0]) + " , X = " + str(req[1]) + " " + res.json()['message'] + "; " + str(len(prioritized_q)) + " remained")
    print('----------------------------------')
    if Environment.service_status == 'to stop':
        Environment.service_status == 'stopped'


def get_insertion_index_1(uid):
    if not prioritized_q:
        return 0

    uids = [rec[0] for rec in prioritized_q]
    if uid not in uids:
        return len(uids)
    else:
        uids.reverse()
        last = len(prioritized_q) - uids.index(uid) - 1
        return last + len(set([prioritized_q[v][0] for v in range(last + 1, len(uids))]))


def get_insertion_index_2(uid):
    if not prioritized_q:
        return 0

    uids = [rec[0] for rec in prioritized_q]
    total_length = len(uids)
    uids.reverse()
    last = total_length - uids.index(uid) - 1 if uid in uids else 0
    user_req_count = uids.count(uid) + 1
    index = user_req_count * (total_length - last - 1) / total_length + last
    return int(index)
