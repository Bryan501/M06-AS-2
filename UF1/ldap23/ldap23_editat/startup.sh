#!/bin/bash

rm -rf /var/lib/ldap/*
rm -rf /etc/ldap/slapd.d/*

slaptest -f /opt/docker/slapd.conf -F /etc/ldap/slapd.d

slapadd -F /etc/ldap/slapd.d -l /opt/docker/edt-org.ldif

chown -R openldap:openldap /etc/ldap/slapd.d /var/lib/ldap

/usr/sbin/slapd -d0
