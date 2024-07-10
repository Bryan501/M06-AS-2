# webdav server

# Utilització d'un imatge Debian com a bases:
FROM debian:latest
LABEL version="1.0"
LABEL author="@edt ASIX-M06"
LABEL subject="WebDav Server: Contingut git 2024"

# Actualiza els repositoris i instal·la els paquets necessaris o per defecte
RUN apt-get update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install procps iproute2 tree nmap vim less passwd git apache2 davfs2

RUN mkdir /opt/docker
COPY * /opt/docker/
RUN chmod +x /opt/docker/startup.sh
WORKDIR /opt/docker

CMD /opt/docker/startup.sh
