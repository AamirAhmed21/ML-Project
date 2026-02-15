FROM python:3.13.3-slim

WORKDIR /application

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN apt update && apt install -y awscli

CMD ["python", "application.py"]
