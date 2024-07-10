# ldapserver
FROM debian:latest
LABEL version="1.0"
LABEL author="@edt ASIX-M06"
LABEL subject="SAMBA server user home's shares"

RUN apt-get update
#ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install procps vim procps nmap tree iproute2 less cifs-utils finger passwd  libnss-ldapd libpam-ldapd nslcd nslcd-utils ldap-utils libpam-mount libpam-pwquality samba samba-client

RUN mkdir /opt/docker

COPY * /opt/docker/
COPY fitxer.sh /opt/docker/
COPY ldap.conf /etc/ldap/
COPY nslcd.conf /etc/
COPY nsswitch.conf /etc/
COPY common-session /etc/pam.d/
COPY pam_mount.conf.xml /etc/security/

RUN chmod +x /opt/docker/startup.sh /opt/docker/usersldap.sh
WORKDIR /opt/docker
CMD /opt/docker/startup.sh && /opt/docker/usersldap.sh

