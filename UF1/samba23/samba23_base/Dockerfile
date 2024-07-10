# SAMBA 2024

FROM debian:latest

LABEL version="1.0"
LABEL author="@edt ASIX-M06"
LABEL subject="SERVIDOR SAMBA"

RUN apt-get update
#ARG DEBIAN_FRONTEND=noninteractive Evitar preguntas a la instalacio
RUN apt-get -y install procps iproute2 tree nmap vim net-tools less finger passwd samba-client samba cifs-utils

RUN mkdir /opt/docker
COPY * /opt/docker/
RUN chmod +x /opt/docker/startup.sh
WORKDIR /opt/docker

CMD /opt/docker/startup.sh


