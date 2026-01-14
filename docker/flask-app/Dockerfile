FROM python:3.9-slim

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY run.py .

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "run.py"] 
