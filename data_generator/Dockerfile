FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY generate_fake_data.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "generate_fake_data.py"]
