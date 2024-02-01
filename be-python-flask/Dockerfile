FROM python:3.12-slim

WORKDIR /long-time-no-see
COPY . /long-time-no-see

RUN pip install poetry
RUN poetry export --output requirements.txt
RUN pip install -r requirements.txt

WORKDIR /long-time-no-see/long_time_no_see/
CMD flask run -h 0.0.0.0 -p 5000