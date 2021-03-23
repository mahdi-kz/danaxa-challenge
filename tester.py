import requests, random

max_request = 1000
user_count = 20

for v in range(max_request):
    uid = random.randint(0, user_count)
    res = requests.post('http://127.0.0.1:5000/api/call',
                        json={"user_id": uid, "x": "Request " + str(v)})
    print("Request " + str(v) + "sent")
