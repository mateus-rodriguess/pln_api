FROM tensorflow/tensorflow:2.8.0

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER root

WORKDIR /code

# install dependencies
RUN apt update && \
    apt install --no-install-recommends -y build-essential musl-dev ca-certificates && \
    apt clean && rm -rf /var/lib/apt/lists/*

# install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# Add entrypoint to the image
COPY entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

# copy project
COPY . .

# RUN entrypoit.sh
CMD /code/entrypoint.sh