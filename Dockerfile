FROM python:3.8-buster

WORKDIR .
COPY requirements.txt /app/
COPY . /app/

WORKDIR /app/
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]