#FROM ubuntu:14.04
FROM base-ubuntu

#ADD http://stedolan.github.io/jq/download/linux64/jq /usr/local/bin/jq
#COPY jq /usr/local/bin/jq

#ADD https://get.docker.io/builds/Linux/x86_64/docker-latest /usr/local/bin/docker
#COPY docker /usr/local/bin/docker

COPY in /opt/resource/in
COPY check /opt/resource/check
COPY out /opt/resource/out
COPY common.py /opt/resource/common.py

RUN chmod +x /opt/resource/in /opt/resource/check /opt/resource/out

#RUN chmod +x /opt/resource/in /opt/resource/check /opt/resource/out && \
#    apt-get update && \
#    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip && \
#    pip3 install docker-py && \
#    apt-get remove -y python3-pip && \
#    apt-get autoremove -y 

