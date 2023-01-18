FROM python:3.10

EXPOSE 8000

WORKDIR /P13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

COPY . .
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000