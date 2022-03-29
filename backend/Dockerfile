FROM python:3.9-slim-buster

WORKDIR /backend

COPY backend/requirements.txt requirements.txt

EXPOSE 5000

RUN pip3 install -r requirements.txt

COPY /backend .

CMD [ "python3", "run.py"]