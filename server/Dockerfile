# syntax=docker/dockerfile:1

FROM ubuntu:21.04
WORKDIR /app
RUN apt update
RUN DEBIAN_FRONTEND="noninteractive" apt install -y software-properties-common python3.9 python3-pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
