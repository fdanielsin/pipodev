FROM python:3.8

COPY . /app

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3 python3-dev

RUN pip install -r requirements.txt

RUN python3 -m pip install --upgrade pip

EXPOSE 1000

CMD [ "python", "main.py" ]