FROM python:3.10-slim AS autogpt-base
RUN apt-get update && apt-get install -y gcc python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
ENV PIP_NO_CACHE_DIR=yes PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD gunicorn resumeWorld.wsgi:application --bind 0.0.0.0:8000
EXPOSE 8000