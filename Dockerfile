# Use the Python 3.11 image from ECR
FROM <your-account-id>.dkr.ecr.<region>.amazonaws.com/python:3.11

# Install system dependencies for R and Python

RUN apt-get update && apt-get install -y \
    libssl-dev \
    nginx \
    libxml2-dev

# Install Python dependencies
RUN pip install gunicorn flask boto3

# Copy the requirements.txt file into the container
COPY scripts_model/requirements_Python.txt  /

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY scripts_model/ /opt/program
COPY scripts_nonmodel/ /opt/program
WORKDIR /opt/program
RUN chmod +x serve
ENTRYPOINT ["python", "/opt/program/serve"]
