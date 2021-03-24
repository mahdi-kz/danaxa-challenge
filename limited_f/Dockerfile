From python:3-slim-stretch
ADD . /danaxa-challenge/limited_f
WORKDIR /danaxa-challenge/limited_f
RUN pip install -r requirement.txt
ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=5001
