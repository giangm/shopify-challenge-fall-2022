FROM python:3.8

## Set working directory to /app
WORKDIR /app

## Copy all files and directories to /app in container
COPY . /app

## Install required libraries in requirements.txt
RUN pip install -r requirements.txt

## Start flask application
CMD ["python3", "run.py"]