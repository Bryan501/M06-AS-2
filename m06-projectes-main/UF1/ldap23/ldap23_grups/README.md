# Imatge personalitzada de Debian per utilizar LDAP

Aquesta imatge de Docker està basada en un Debian i conté el procés de com instal·lar el servei
LDAP, utilitzant esquemes i el phpldapadmin.

## Dockerfile

L'arxiu "Dockerfile" definirà els passos a seguir per a la construcció de l'imatge Docker.

```Dockerfile
# LDAP SERVER 2023

# Creació d'un Debian personalitzat:

FROM debian:latest
LABEL version="1.0"
LABEL author="@edt ASIX-M06"
LABEL subject="ldap.edt.org 2023"

# Actualitzem el container e instal·lem les eines necessaries:

RUN apt-get update
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y procps iproute2 vim tree nmap ldap-utils slapd less

#Creem, copiem, fem executable, executem primer el que volem i que port volem que el container escolti:

RUN mkdir /opt/docker
COPY * /opt/docker/
RUN chmod +x /opt/docker/startup.sh
WORKDIR /opt/docker
CMD /opt/docker/startup.sh
EXPOSE 389
```
## Startup.sh

L'arxiu "Startup.sh" s'executarà mitjançant el "Dockerfile" sense necesitat de fer totes les comandes des d'adins del container. On farem els següents passos a seguir:

1) Esborrar els directoris de configuració i de dades.
2) Generar el directori de configuració dinàmica slapd.d a partir del fitxer de configuració slapd.conf.
3) Injectar a baix nivell les dades de la BD 'populate' de l'organització dc=edt,dc=org.
4) Assignar la propietat i grup del directori de ddaes i de configuració a l'usuari openldap.
5) Engegar el servei slapd amb el paràmetre que fa debug per mantenir-lo engegat en foreground.

```bash
#! /bin/bash

echo "Inicialitzant la BD ldap edt.org"

rm -rf /etc/ldap/slapd.d/* /var/lib/ldap/*
slaptest -f slapd.conf -F /etc/ldap/slapd.d
slapadd -F /etc/ldap/slapd.d/ -l edt-org.ldif 
chown -R openldap:openldap /etc/ldap/slapd.d /var/lib/ldap
slapcat

cp /opt/docker/ldap.conf /etc/ldap/ldap.conf
/usr/sbin/slapd -d0
```
## edt-org.ldif

Aquest arxiu "edt.org.ldif" descriu la configuració de l'estructura d'un directori LDAP, incloent unitats organitzatives (OU), comptes d'usuaris (uid), grups (cn) i les seves relacions. Defineix diferents OU per a maquines, clients, productes, usuaris, grups, etc., i especifica detalls com els noms, números d'identificació, directoris personals i contrasenyes encriptades dels usuaris. També estableix relacions de pertinença dels usuaris als grups corresponents.

```ldif
dn: dc=edt,dc=org
dc: edt
description: Escola del treball de Barcelona
objectClass: dcObject
objectClass: organization
o: edt.org

dn: ou=maquines,dc=edt,dc=org
ou: maquines
description: Container per a maquines linux
objectclass: organizationalunit

dn: ou=clients,dc=edt,dc=org
ou: clients
description: Container per a clients linux
objectclass: organizationalunit

dn: ou=productes,dc=edt,dc=org
ou: productes
description: Container per a productes linux
objectclass: organizationalunit

dn: ou=usuaris,dc=edt,dc=org
ou: usuaris
description: Container per usuaris del sistema linux
objectclass: organizationalunit

dn: ou=grups,dc=edt,dc=org
ou: grups
description: Container per a grups
objectclass: organizationalunit

dn: ou=Asix,dc=edt,dc=org
ou: Asix
description: Container per els asix del sistema linux
objectclass: organizationalunit

dn: ou=AntiAsix,dc=edt,dc=org
ou: Asix
description: Container per els antiasix del sistema linux
objectclass: organizationalunit

dn: uid=pau,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: Pau Pou
cn: Pauet Pou
sn: Pou
homephone: 555-222-2220
mail: pau@edt.org
description: Watch out for this guy
ou: professors
uid: pau
uidNumber: 5000
gidNumber: 601
homeDirectory: /tmp/home/pau
userPassword: {SSHA}NDkipesNQqTFDgGJfyraLz/csZAIlk2/

dn: uid=pere,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: Pere Pou
sn: Pou
homephone: 555-222-2221
mail: pere@edt.org
description: Watch out for this guy
ou: professors
uid: pere
uidNumber: 5001
gidNumber: 601
homeDirectory: /tmp/home/pere
userPassword: {SSHA}ghmtRL11YtXoUhIP7z6f7nb8RCNadFe+

dn: uid=anna,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: Anna Pou
cn: Anita Pou
sn: Pou
homephone: 555-222-2222
mail: anna@edt.org
description: Watch out for this girl
ou: alumnes
uid: anna
uidNumber: 5002
gidNumber: 600
homeDirectory: /tmp/home/anna
userPassword: {SSHA}Bm4B3Bu/fuH6Bby9lgxfFAwLYrK0RbOq

dn: uid=marta,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: Marta Mas
sn: Mas
homephone: 555-222-2223
mail: marta@edt.org
description: Watch out for this girl
ou: alumnes
uid: marta
uidNumber: 5003
gidNumber: 600
homeDirectory: /tmp/home/marta
userPassword: {SSHA}9+1F2f5vcW8z/tmSzYNWdlz5GbDCyoOw

dn: uid=jordi,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: Jordi Mas
cn: Giorgios Mas
sn: Mas
homephone: 555-222-2224
mail: jordi@edt.org
description: Watch out for this guy
ou: alumnes
ou: Profes
uid: jordi
uidNumber: 5004
gidNumber: 600
homeDirectory: /tmp/home/jordi
userPassword: {SSHA}T5jrMgpJwZZgu0azkLIVoYhiG08/KGUv

dn: uid=admin,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: Administrador Sistema
cn: System Admin
sn: System
homephone: 555-222-2225
mail: anna@edt.org
description: Watch out for this admin
ou: system
ou: admin
uid: admin
uidNumber: 10
gidNumber: 27
homeDirectory: /tmp/home/admin
userPassword: {SSHA}4mS0FycWc5bkpW8/a396SGNDTQUlFSX3

dn: uid=Pol Sanjurjo,ou=Asix,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: Polete
cn: Pop
sn: Sanjurjo
homephone: 555-222-2225
mail: polsanjurjo@edt.org
description: Aquest noi es ros
ou: Asix
ou: AntiAsix
uid: admin
uidNumber: 10
gidNumber: 601
homeDirectory: /tmp/home/sanjurjo
userPassword: {SSHA}cDDURbhITwNmvgIIBms12BVnCTs8ydgN

dn: uid=Eustaqui Eus,ou=AntiAsix,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: Eustaqui Eus
cn: Eustaqui Eus Us
sn: Eustaqui Eus
homephone: 555-222-2224
mail: esutaqui@edt.org
description: Watch out for this guy
ou: AntiAsix
ou: Asix
uid: Eustaqui Eus
uidNumber: 5004
gidNumber: 27
homeDirectory: /tmp/home/eustaqui
userPassword: {SSHA}s+k4NK6fSwI3JtJ4pZUE3fcoZTZ2hUnR

# --------------------UserXX-----------------------------

dn: uid=user01,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user01
sn: usuari01
description: Primer usuari de 1asix
ou: 1asix
uid: user01
uidNumber: 2001
gidNumber: 610
homeDirectory: /home/user01
userPassword: {SSHA}tWkj/NWcStWT0u+u4HYvf23eaRhYtPYR

dn: uid=user02,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user02
sn: usuari02
description: Segon usuari de 1asix
ou: 1asix
uid: user02
uidNumber: 2002
gidNumber: 610
homeDirectory: /home/user02
userPassword: {SSHA}OVz4p9rsOCmuzUH49uUx/PTQHidAX2NX

dn: uid=user03,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user03
sn: usuari03
description: Tercer usuari de 1asix
ou: 1asix
uid: user02
uidNumber: 2003
gidNumber: 610
homeDirectory: /home/user03
userPassword: {SSHA}AtGV6D5P/YQ07XN2c+Bcex84dSFn8odd

dn: uid=user04,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user04
sn: usuari04
description: Primer usuari de 1hiaw
ou: 1hiaw
uid: user04
uidNumber: 3001
gidNumber: 614
homeDirectory: /home/user04
userPassword: {SSHA}QWsbNGIAVR8b36H4Lj36wm2FXpejmjFk

dn: uid=user05,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user05
sn: usuari05
description: Segon usuari de 1hiaw
ou: 1hiaw
uid: user05
uidNumber: 3002
gidNumber: 614
homeDirectory: /home/user05
userPassword: {SSHA}kzW0zp/+2Cbc+8tJYl26+iGSuY58TNa/

dn: uid=user06,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user06
sn: usuari06
homephone: 555-222-0006
mail: user06@edt.org
description: Tercer usuari de 1hiaw
ou: 1hiaw
uid: user06
uidNumber: 3003
gidNumber: 614
homeDirectory: /home/user06
userPassword: {SSHA}jzwpD9kkG0c0gYjGgSRpzFUoxzXx9Tla

dn: uid=user07,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user07
sn: usuari07
description: Primer usuari de 2asix
ou: 2asix
uid: user07
uidNumber: 4001
gidNumber: 611
homeDirectory: /home/user07
userPassword: {SSHA}49vxSqSzW1vcXuPB0Ty5VQhi3MBeyla5

dn: uid=user08,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user08
sn: usuari08
description: Segon usuari de 2asix
ou: 2asix
uid: user08
uidNumber: 4002
gidNumber: 611
homeDirectory: /home/user08
userPassword: {SSHA}pUUjnlChFQlqGlp2qMNtpuj5VxgbcKs9

dn: uid=user09,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user09
sn: usuari09
description: Tercer usuari de 2asix
ou: 2asix
uid: user09
uidNumber: 4003
gidNumber: 611
homeDirectory: /home/user09
userPassword: {SSHA}qTY2/PIw9DsCtNnDZK/u4rQjHTGSaBsI

dn: uid=user10,ou=usuaris,dc=edt,dc=org
objectclass: posixAccount
objectclass: inetOrgPerson
cn: user10
sn: usuari10
description: Quart usuari de 2asix
ou: 2asix
uid: user10
uidNumber: 4004
gidNumber: 611
homeDirectory: /home/user10
userPassword: {SSHA}HSkB11eOgrMaky1iAmCZiFDDLkTdmSLU

# -----------------GRUPS------------------------------

dn: cn=professors,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: professors
gidNumber: 601
description: Grup dels professors
memberUid: pau
memberUid: pere

dn: cn=alumnes,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: alumnes
gidNumber: 600
description: Grup dels alumnes
memberUid: anna
memberUid: marta
memberUid: jordi

dn: cn=1asix,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: 1asix
gidNumber: 610
description: Grup dels usuaris de 1asix
memberUid: user01
memberUid: user02
memberUid: user03

dn: cn=2asix,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: 2asix
gidNumber: 611
description: El grup dels usuaris de 2asix
memberUid: user07
memberUid: user08
memberUid: user09
memberUid: user10

dn: cn=sudo,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: sudo
gidNumber: 27
description: Grup dels privilegiats
memberUid: admin
memberUid: Eustaqui Eus

dn: cn=1wiam,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: 1wiam
gidNumber: 612
description: Grup dels usuaris de 1wiam

dn: cn=2wiam,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: 2wiam
gidNumber: 613
description: Grup dels usuaris de 2wiam

dn: cn=1hiaw,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: 1hiaw
gidNumber: 614
description: Grup dels usuaris de 1hiaw
memberUid: user04
memberUid: user05
memberUid: user06
```

## slapd.conf

L'arxiu "slapd.conf" està definida per el següent contingut amb els includes necessaris:

```bash
#
# See slapd.conf(5) for details on configuration options.
# This file should NOT be world readable.
#
# debian packages: slapd ldap-utils

include		/etc/ldap/schema/core.schema
include		/etc/ldap/schema/cosine.schema
include		/etc/ldap/schema/inetorgperson.schema
include		/etc/ldap/schema/misc.schema
include		/etc/ldap/schema/nis.schema
include		/etc/ldap/schema/openldap.schema

# Allow LDAPv2 client connections.  This is NOT the default.
allow bind_v2

pidfile		/var/run/slapd/slapd.pid
#argsfile	/var/run/openldap/slapd.args

modulepath /usr/lib/ldap
moduleload back_mdb.la
moduleload back_monitor.la

# ----------------------------------------------------------------------
database mdb
suffix "dc=edt,dc=org"
rootdn "cn=Manager,dc=edt,dc=org"
#rootpw secret
rootpw {SSHA}oAtPEpCsAdk6SLqmqv+6fkqm2EHELq32
directory /var/lib/ldap
index objectClass eq,pres
access to * by self write by * read
# ----------------------------------------------------------------------
database config
rootdn "cn=Sysadmin,cn=config"
rootpw {SSHA}vwpQxtzc7yLsGg8K7fm02p2Fhox/PFP4
# el passwd es syskey
# ----------------------------------------------------------------------
database monitor
access to *
       by dn.exact="cn=Manager,dc=edt,dc=org" read
       by * none
```

## ldap.conf

L'arxiu "ldap.conf" configura la connexió i el comportament de LDAP, establint paràmetres com la base de cerca (BASE), la ubicació del servidor (URI) i opcions com límits de mida i temps, a més de configuracions per a certificats TLS. En aquest cas específic, defineix la base de cerca com a dc=edt,dc=org i el servidor LDAP URI ldap://ldap.edt.org. A més, especifica la ruta del certificat TLS a TLS_CACERT com /etc/ssl/certs/ca-certificates.crt.

```bash
#
# LDAP Defaults
#

# See ldap.conf(5) for details
# This file should be world readable but not world writable.

#BASE	dc=example,dc=com
#URI	ldap://ldap.example.com ldap://ldap-provider.example.com:666

#SIZELIMIT	12
#TIMELIMIT	15
#DEREF		never

# TLS certificates (needed for GnuTLS)
TLS_CACERT	/etc/ssl/certs/ca-certificates.crt

BASE dc=edt,dc=org
URI  ldap://ldap.edt.org
```

## docker-compose.yml

Aquest fitxer docker-compose.yml descriu la configuració per a dos serveis Docker: un servidor LDAP i una interfície web per a la gestió d'aquest servidor LDAP.

· El servei "ldap" utilitza una imatge anomenada "bryan501/ldap23:latestv2" per crear un contenidor anomenat "ldap.edt.org". Aquest servei s'exposa al port 389 
  del host i utilitza una xarxa denominada "2hisx".

· El servei "phpldapadmin" fa servir una imatge anomenada "bryan501/phpldapadmin23:v2" per a un contenidor amb el nom de "php.edt.org". Aquest servei s'exposa 
  al port 80 del host i també utilitza la xarxa "2hisx".

· Finalment, es defineix la xarxa "2hisx" que connecta els dos serveis i permet la comunicació entre ells.

```bash
version: "3.1"
services:
  ldap:
    image: bryan501/ldap23:latestv2
    container_name: ldap.edt.org
    hostname: ldap.edt.org
    ports:
      - "389:389"
    networks:
      - 2hisx
  phpldapadmin:
    image: bryan501/phpldapadmin23:v2
    container_name: php.edt.org
    hostname: php.edt.org
    ports:
      - "80:80"
    networks:
      - 2hisx
networks:
  2hisx:
```

## Desenvolupament

#-----------------------------------------------------------
#-----------------------------------------------------------

05_practica_grups

Crear una nova imatge ldap: edtasixm06/ldap23:grups

    ● Fet també que sigui la imatge latest edtasixm06/ldap23:latest
    ● modificar el fitxer edt.org.ldif per afegir una ou grups.
    ● definir els següents grups:
        ○ alumnes(600), professors(601), 1asix(610), 2asix(611),
        sudo(27), 1wiam(612), 2wiam(613), 1hiaw(614).

    ● Els grups han de ser elements posixGroup
    ● verificar el llistat dels usuaris i grups i la coherència de dades entre els usuaris que ja teníem i els nous grups creats.
    ● Modificar el startup.sh perquè el servei ldap escolti per tots els protocols: ldap ldaps i ldapi.

Creació de grups

Implementar a la base de dades edt.org els següents canvis:

1. Modificar les RDN dels usuaris per tal de que s’identifiquin en el seu DN per el seu uid. Per exemple ‘cn=Pere Pou,ou=usuaris,dc=edt,dc=org’ passa a ser ‘uid=pere,ou=usuaris,dc=edt,dc=org’

2. Afegir una entitat organizationalUnit anomenada grups que servirà per contenir els grups d’usuaris.
dn: ou=grups,dc=edt,dc=org
ou: groups
description: Container per a grups
objectclass: organizationalunit

3. Crear cadascun dels grups amb entitats de tipus posixAccount. Podeu consultar ldapwiki / phpldapadmin per observar l’estructura d’aquest objectClass. Cal crearà els grups:
    ● professors / 601 (no podem usar el GID 100 que és users)
    ● alumnes / 600
    ● 1asix / 610
    ● 2asix / 611
    ● sudo / 27
    ● 1wiam / 612
    ● 2wiam / 613
    ● 1hiaw / 614

Exemple del grup 2asix:

dn: cn=2asix,ou=grups,dc=edt,dc=org
objectclass: posixGroup
cn: 2asix
gidNumber: 611
description: Grup de 2asix
memberUid: user06
memberUid: user07
memberUid: user08
memberUid: user09
memberUid: user10

Cal assignar cada un dels usuaris (els ‘normals’ i els userxx) al seu grup corresponent segons el seu atribut gidNumber.
Assegurar-se de modificar els usuaris que tenen assignat el gidNumber a 100 i posar el nou valor 601.

4. Modificar usuari admin perquè sigui del grup 27 sudo.

5. Eliminar de la configuració de slapd.conf els includes dels schema que no siguin
necessaris per la base de dades edt.org.

6. Pujeu la imatge al DockerHub, al Git i poseu-li la documentació/README
descriptiva.

#-----------------------------------------------------------
#-----------------------------------------------------------

Per crear la imatge, farem la següent ordre:
```bash
docker build -t bryan501/ldap23:latestv2 .
```
Generem la imatge:
```bash
 docker run --rm --name ldap.edt.org -h ldap.edt.org --net 2hisx -p 389:389 -it bryan501/ldap23:latestv2
```
Generem tambe el phpldapadmin:
```bash
docker run --rm --name php.edt.org -h php.edt.org --net 2hisx -p 80:80 -it bryan501/phpldapadmin23:v2
```

Si volem Ens estalviem els dos "docker run":
```bash
docker compose up -d
```
Verifiquem al phpldapadmin:
```html
http://localhost/phpldapadmin
```
Fem stop i esborrem els serveis, al haver fet el docker compose:
```bash
docker compose down
```

