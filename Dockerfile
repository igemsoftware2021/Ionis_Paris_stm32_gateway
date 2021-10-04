FROM python:3.9.7-bullseye

# setup workdir
WORKDIR /app

# copy only requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD python src/main.py