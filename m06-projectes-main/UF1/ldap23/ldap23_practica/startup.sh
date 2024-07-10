#! /bin/bash

echo "Inicialització BD ldap edt.org"

rm -rf /etc/ldap/slapd.d/* /var/lib/ldap/*
slaptest -f slapd.conf -F /etc/ldap/slapd.d
slapadd -F /etc/ldap/slapd.d/ -l edt-org.ldif 
chown -R openldap:openldap /etc/ldap/slapd.d /var/lib/ldap
slapcat

cp /opt/docker/ldap.conf /etc/ldap/ldap.conf
/usr/sbin/slapd -d0
