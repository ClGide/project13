FROM python:3.10

EXPOSE 8000

WORKDIR /P13

COPY . .
RUN pip install -r requirements.txt
