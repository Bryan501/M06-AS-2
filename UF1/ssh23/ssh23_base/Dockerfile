# ldap + pam + ssh

FROM debian:latest

LABEL version="1.0"
LABEL author="@edt ASIX-M06"
LABEL subject="SERVIDOR SSH"

RUN apt-get update
#ARG DEBIAN_FRONTEND=noninteractive Evitar preguntas a la instalacio
RUN apt-get -y install procps iproute2 tree nmap vim less finger passwd libpam-ldapd libpam-pwquality libpam-mount nslcd nslcd-utils ldap-utils libnss-ldap openssh-server openssh-client

RUN mkdir /opt/docker
COPY * /opt/docker/
RUN chmod +x /opt/docker/startup.sh
WORKDIR /opt/docker

CMD /opt/docker/startup.sh

