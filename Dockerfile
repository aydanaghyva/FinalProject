# FROM python:3.12

# WORKDIR /app

# # Install dependencies
# COPY requirements.txt /app/
# RUN pip install -r requirements.txt
# RUN pip install celery  # Make sure Celery is installed

# # Copy project files
# COPY . /app/
# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory
WORKDIR /app
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables (optional)
ENV PYTHONUNBUFFERED 1

# Command to run Celery
CMD ["celery", "-A", "djangoexamproject", "worker", "--loglevel=info"]
