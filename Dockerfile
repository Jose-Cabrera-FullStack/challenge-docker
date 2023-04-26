FROM python:3.8.4-slim-buster

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y build-essential

COPY find_matching_pair.py /usr/src/app/
COPY decode_message_hex.py /usr/src/app/
COPY tests /usr/src/app/tests/

CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-p", "*_test.py", "-f"]
