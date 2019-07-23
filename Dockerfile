FROM python:3.7-alpine

COPY src/requirements.txt /

RUN pip install -r /requirements.txt --disable-pip-version-check

COPY src/ /app
WORKDIR /app

CMD ["python", "app.py"]