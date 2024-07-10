# ldap + pam + samba

FROM debian:latest
LABEL version="1.0"
LABEL author="@edt ASIX-M06"
LABEL subject="PAM HOST 2024"

RUN apt-get update
#ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y install procps iproute2 tree nmap vim less finger passwd libnss-ldapd libpam-ldapd libpam-pwquality libpam-mount nslcd nslcd-utils ldap-utils samba-client cifs-utils

RUN mkdir /opt/docker
COPY * /opt/docker/

COPY ldap.conf /etc/ldap/
COPY nslcd.conf /etc/
COPY nsswitch.conf /etc/
COPY common-session /etc/pam.d/
COPY pam_mount.conf.xml /etc/security/

RUN chmod +x /opt/docker/startup.sh
WORKDIR /opt/docker
CMD /opt/docker/startup.sh

