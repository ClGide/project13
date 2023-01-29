FROM python:3.10

WORKDIR /P13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG=0
ENV PORT 8000

COPY . .
RUN pip install -r requirements.txt

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000
