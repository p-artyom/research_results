FROM python:3.11.5

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "manage.py", "runserver", "0:8000"]