#!/bin/bash
#
#1) Esborrar els directoris de configuració i de dades
#2) Generar el directori de configuració dinàmica slapd.d a partir del fitxer de configuració slapd.conf
#3) Injectar a baix nivell les dades de la BD 'populate' de l'organització dc=edt,dc=org
#4) Assignar la propietat i grup del directori de ddaes i de configuració a l'usuari openldap
#5) Engegar el servei slapd amb el paràmetre que fa debug per mantenir-lo engegat en foreground
#

rm -rf /var/lib/ldap/*
rm -rf /etc/ldap/slapd.d/*

slaptest -f /opt/docker/slapd.conf -F /etc/ldap/slapd.d
slapadd -F /etc/ldap/slapd.d -l /opt/docker/edt-org.ldif
chown -R openldap:openldap /etc/ldap/slpad.d /var/lib/ldap
