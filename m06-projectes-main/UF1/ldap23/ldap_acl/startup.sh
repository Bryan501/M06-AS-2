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

# Fa una prova on especefica el fitxer de configuració a una carpeta on és generaran els fitxers
# després de les proves.

slaptest -f /opt/docker/slapd.conf -F /etc/ldap/slapd.d

# Afegeix el contingut a la base de dades indicant la carpeta on es troben els fitxers de configuració
# generats i indica l'arxiu LDIF que conté les dades a afegir a la base de dades.

slapadd -F /etc/ldap/slapd.d -l /opt/docker/edt-org.ldif

# Canvia el propietari

chown -R openldap:openldap /etc/ldap/slapd.d /var/lib/ldap

# Executa el servidor LDAP, habilitant la sortida en debug amb nivell 0
cp /opt/docker/ldap.conf /etc/ldap/ldap.conf

/usr/sbin/slapd -d0
