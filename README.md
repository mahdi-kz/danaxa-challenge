# danaxa-challenge
There are two services implemented.

__limited_f__: A service receives a request and responds in 1 second.

__Intermediary__: The service which receives requests, prioritizes, and send to _limited_f_ service.

And there is a python file named _tester.py_ when run sends a bunch of requests to the service _Intermediary_. 

## To run services manually
### Run Intermediary Service
Navigate into ___intermidiary___ > ___app___ folder:
```bash
cd /danaxa-challenge/intermediary/app
```
Open the file __environment.py__. Uncomment the first url to connect to __limited_f__ service and comment the second one. The file should be like:
```python
class Environment:
    service_status = service_status['stopped']
    limited_f_url = 'http://127.0.0.1:5001/limited/call'         # If the services run manually
    # limited_f_url = 'http://limited_f:5001/limited/call'    # If the services run dockerized
```

Get back and create and setup a Virtual Environment:
```bash
cd ..
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```

Install requirements:
```bash
sudo apt install python3-pip
sudo pip3 install -r requirements.txt
```
Run service
```bash
flask run -h '0.0.0.0'
```

### Run limited_f Service
The same as that for _Intermediary_ service

```bash
cd /danaxa-challenge/limited_f/
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
sudo apt install python3-pip
sudo pip3 install -r requirements.txt
flask run -h '0.0.0.0'
```

### Test the service
From terminal _start_ the intermediary service
```bash
curl -X POST http://127.0.0.1:5000/api/start
```
Navigate to the root of the project and run the tester
```bash
cd /danaxa-challenge/
python3 tester.py
```

### Start/Stop the intermediary service
__Start__
```bash
curl -X POST http://127.0.0.1:5000/api/start
```
__Stop__
```bash
curl -X POST http://127.0.0.1:5000/api/stop
```

## To Run dockerized
Navigate into ___intermidiary___ > ___app___ folder:
```bash
cd /danaxa-challenge/intermediary/app
```
Open the file __environment.py__.  Uncomment the second url to connect to __limited_f__ service and comment the first one. The file should be like:
```python
class Environment:
    service_status = service_status['stopped']
    # limited_f_url = 'http://127.0.0.1:5001/limited/call'         # If the services run manually
    limited_f_url = 'http://limited_f:5001/limited/call'    # If the services run dockerized
```
Navigate to the root of the project and run the _run.sh_ script
```bash
cd /danaxa-challenge
sudo chmod 777 run.sh
sudo ./run.sh
```