FROM python:3.8.10

ENV PYTHONUNBUFFERED=1

WORKDIR /covid

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]