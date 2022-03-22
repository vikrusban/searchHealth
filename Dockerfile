FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3-pip
ADD config.py /opt/searchHealth/config.py
ADD list_url.txt /opt/searchHealth/list_url.txt
ADD main.py /opt/searchHealth/main.py
ADD requirements.txt /opt/searchHealth/requirements.txt
RUN cd /opt/searchHealth/ && pip3 install -r requirements.txt
WORKDIR /opt/searchHealth
ENTRYPOINT ["python3", "main.py"]
VOLUME /opt/searchHealth