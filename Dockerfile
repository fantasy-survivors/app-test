FROM python:3.8-slim

WORKDIR /app

# Install essential libraries and tools
RUN apt-get update && \
    apt-get install -y build-essential

COPY requirements.txt .
# COPY /scripts /app/scripts
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
