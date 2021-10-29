FROM python:3.10.0-slim-buster

RUN pip install --upgrade pip

COPY dockerfiles/demo/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY dockerfiles/demo/. /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
