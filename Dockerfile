FROM python:3.8-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER root
WORKDIR /code

# install dependencies
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc g++  gfortran musl-dev ca-certificates && \
    apt clean && rm -rf /var/lib/apt/lists/*


# install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .
