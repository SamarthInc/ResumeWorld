FROM python:latest
RUN apt-get update && apt-get install -y gcc python3-dev && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y cmake
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN [ "python", "-c", "import nltk; nltk.download('stopwords')" ]
RUN [ "python", "-c", "import nltk; nltk.download('punkt')" ]
RUN [ "python", "-c", "import nltk; nltk.download('wordnet')" ]
COPY . .
CMD gunicorn resumeWorld.wsgi:application --bind 0.0.0.0:8000
EXPOSE 8000