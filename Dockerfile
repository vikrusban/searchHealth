FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3-pip
ADD main.py /opt/searchHealth/main.py
ADD async_collect_data.py /opt/searchHealth/async_collect_data.py
ADD requirements.txt /opt/searchHealth/requirements.txt
RUN cd /opt/searchHealth/ && pip3 install -r requirements.txt
WORKDIR /opt/searchHealth
ENTRYPOINT ["python3", "main.py"]
VOLUME /opt/searchHealth