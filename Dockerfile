# Use the Python 3.11 image from ECR
FROM public.ecr.aws/v3z5t7a3/my_repo_xgboost_test:python-3.11

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
RUN pip install --no-cache-dir -r scripts_model/requirements_Python.txt

# Application port
EXPOSE 8000
# Prometheus metrics port
EXPOSE 8001  

CMD ["gunicorn", "-c", "gunicorn_config.py", "scripts_nonmodel.wsgi:app"]
