ARG Account_id
ARG region

# Use the Python 3.11 image from ECR
FROM <Account_id>.dkr.ecr.<region>.amazonaws.com/python:3.11

WORKDIR /app

COPY . /app

# Install system dependencies for R and Python

RUN apt-get update && apt-get install -y \
    libssl-dev \
    nginx \
    libxml2-dev

# Install Python dependencies
RUN pip install gunicorn flask  prometheus_client psutil

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements_Python.txt

EXPOSE 8000  # Application port
EXPOSE 8001  # Prometheus metrics port

CMD ["gunicorn", "-b", "0.0.0.0:8000", "wsgi:app"]
