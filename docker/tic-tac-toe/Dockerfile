FROM python:3.14-slim

WORKDIR /app

RUN pip install flask==3.0.3

copy . .

EXPOSE 5000

CMD ["python", "app.py"]
