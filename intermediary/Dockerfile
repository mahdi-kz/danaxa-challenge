From python:3-slim-stretch
ADD . /danaxa-challenge/intermediary
WORKDIR /danaxa-challenge/intermediary
RUN pip3 install -r requirement.txt
ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=5000
