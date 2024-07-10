# Imatge personalitzada de Debian per utilizar LDAP

Aquesta imatge de Docker està basada en un Debian i conté el procés de com instal·lar el servei
LDAP, utilitzant esquemes i el phpldapadmin.

## Dockerfile

L'arxiu "Dockerfile" definirà els passos a seguir per a la construcció de l'imatge Docker.

## Startup.sh

L'arxiu "Startup.sh" s'executarà mitjançant el "Dockerfile" sense necesitat de fer totes les comandes des d'adins del container. On farem els següents passos a seguir:

1) Esborrar els directoris de configuració i de dades.
2) Generar el directori de configuració dinàmica slapd.d a partir del fitxer de configuració slapd.conf.
3) Injectar a baix nivell les dades de la BD 'populate' de l'organització dc=edt,dc=org.
4) Assignar la propietat i grup del directori de ddaes i de configuració a l'usuari openldap.
5) Engegar el servei slapd amb el paràmetre que fa debug per mantenir-lo engegat en foreground.

## edt-org.ldif

L'arxiu "edt-org.ldif" tindrà les entitats que volem on  s'utilitzarà mitjançant el "startup.sh"  per agafar les nostres entitats (les dades) i substituir-les per les de defecte. On afegirem unes noves dades que representin l'esquema utilitzat

## slapd.conf

L'arxiu "slapd.conf" està definida per el següent contingut:

```bash
include		/etc/ldap/schema/core.schema
include		/etc/ldap/schema/cosine.schema
include		/etc/ldap/schema/inetorgperson.schema
include		/etc/ldap/schema/misc.schema
include		/etc/ldap/schema/nis.schema
include		/etc/ldap/schema/openldap.schema
include		/opt/docker/projecte.schema # El nostre schema
```

## projecte.schema

L'arxiu "projecte.schema" tendra la nostra configuració personalitzafa de com volem configurar la nostre base de dades al veurel dins amb el phpldapadmin. Contindra el següent contingut:

# Tipus d'Atributs:

    'x-nom':

        Descripció: Nom(s) dels estudiants
        Tipus d'igualtat: Coincidència sense distinció de majúscules/minúscules
        Regla de coincidència de subcadena: Coincidència sense distinció de majúscules/minúscules
        Sintaxi: Cadena de directori
        Valor únic

    'x-grup':

        Descripció: Grup(s) dels estudiants
        Tipus d'igualtat: Coincidència sense distinció de majúscules/minúscules
        Regla de coincidència de subcadena: Coincidència sense distinció de majúscules/minúscules
        Sintaxi: Cadena de directori
        Valor únic

    'x-company':

        Descripció: Company(s) de l'estudiant
        Sintaxi: Cadena de directori
        Valor únic

    'x-projecte':

        Descripció: Actiu True/False del projecte
        Sintaxi: Booleà
        Valor únic
    
    'x-foto':

        Descripció: Foto(s) dels estudiants
        Sintaxi: Cadena octet (usualment per a imatges)

    'x-inf':

        Descripció: Informació dels projectes
        Sintaxi: Cadenes de caràcters

# Classes d'Objectes:

    'x-estudiant':

        Descripció: Institut de Pedralbes GG
        Estructural
        Heretat de: TOP
        Deure: uid, x-nom, x-grup, x-projecte
        Pot: x-foto, x-inf
    
    'x-companyInfo':

        Descripció: Informació de la companyia
        Auxiliar
        Heretat de: TOP
        Pot: x-company 

En resum: 
    Aquest esquema proporciona una estructura per emmagatzemar informació relativa als estudiants, incloent-hi els seus noms, grups, estat dels projectes, entre altres elements rellevants. A més, permet la inclusió d'informació específica de les empreses relacionades amb els estudiants, oferint un marc per gestionar aquesta informació dins del context de l'Institut de Pedralbes GG.

## Desenvolupament

Passos a realitzar el desenvolupament:

- Pujar-la al git

- Pujar-la al dockerhub

- Generar els README.md apropiats

- Crear un schema amb:

- Un nou objecte STRUCTURAL

- Un nou objecte AUXILIARU

- Cada objecte ha de tenir almenys 3 nous atributs.

- Heu d’utilitzar almenys els atributes de tipus boolean, foto (imatge jpeg) i binary per contenir documents pdf.

- Crear una nova ou anomenada practica.

- Crear almenys 3 entitats noves dins de ou=practica que siguin dels objectClass definits en l’schema. 

- Assegurar-se de omplir amb dades reals la foto i el pdf.

- Eliminar del slapd.conf tots els schema que no facin falta, deixar només els imprescindibles

- Visualitzeu amb phpldapadmin les dades, observeu l’schema i verifiqueu la foto i el pdf.

Crearem un objecte STRUCTURAL I AUXILIARU al schema:
```bash

objectClass (1.1.2.1.1 NAME 'x-estudiant'
	DESC 'Institut de Pedralbes GG'
        SUP TOP
	STRUCTURAL
	MUST ( uid $ x-nom $ x-grup $ x-projecte )
	MAY ( x-foto $ x-inf )  )

objectClass (1.1.2.2.2 NAME 'x-companyInfo'
	DESC 'Informació del company'
	SUP TOP
    	AUXILIARY
    	MAY x-company )

```
Afegim el atrbiuts al schema amb les especificacions corresponents:
```bash

attributetype (1.1.2.1.1.1 NAME 'x-nom'
	DESC 'Nom(s) dels estudiants'
	EQUALITY caseIgnoreMatch
	SUBSTR caseIgnoreSubstringsMatch
	SYNTAX 1.3.6.1.4.1.1466.115.121.1.15
	SINGLE-VALUE )

attributetype (1.1.2.1.1.2 NAME 'x-grup'
	DESC 'Grup(s) dels estudiants'
	EQUALITY caseIgnoreMatch
	SUBSTR caseIgnoreSubstringsMatch
	SYNTAX 1.3.6.1.4.1.1466.115.121.1.15
	SINGLE-VALUE )

attributetype (1.1.2.1.1.3 NAME 'x-company'
        DESC 'Company(s) del estudiant'
        SYNTAX 1.3.6.1.4.1.1466.115.121.1.15
        SINGLE-VALUE )

attributetype (1.1.2.1.1.4 NAME 'x-projecte'
	DESC 'Actiu True/False'
	SYNTAX 1.3.6.1.4.1.1466.115.121.1.7
	SINGLE-VALUE )

attributetype (1.1.2.1.1.5 NAME 'x-foto'
	DESC 'Foto(s) dels estudiants'
	SYNTAX 1.3.6.1.4.1.1466.115.121.1.28 )

attributetype (1.1.2.1.1.6 NAME 'x-inf'
	DESC 'Informació dels projectes'
	SYNTAX 1.3.6.1.4.1.1466.115.121.1.5 )

```
Afegir les noves dades al edt-org.ldif:
```bash
dn: ou=practiques,dc=edt,dc=org
ou: practiques
description: Container dels estudiants dels projectes
objectclass: organizationalunit

# Entitats amb objectClass 'x-estudiant' per a la OU 'practiques'
dn: uid=Pol Sanjurjo,ou=practiques,dc=edt,dc=org
objectClass: x-estudiant
objectClass: x-companyInfo
x-nom: Pol Sanjurjo
x-grup: GrupPracticaA
x-projecte: TRUE
x-company: TRUE
x-foto:< file:/opt/docker/PolSanjurjo.jpg
x-inf:< file:/opt/docker/GrupPracticaA.pdf

dn: uid=Marc Melendez,ou=practiques,dc=edt,dc=org
objectClass: x-estudiant
objectClass: x-companyInfo
x-nom: Pol Sanjurjo
x-grup: GrupPracticaB
x-projecte: FALSE
x-company: FALSE
x-foto:< file:/opt/docker/MarcMelendez.jpeg
x-inf:< file:/opt/docker/GrupPracticaB.pdf

dn: uid=Aleix Pedraforca,ou=practiques,dc=edt,dc=org
objectClass: x-estudiant
objectClass: x-companyInfo
x-nom: Pol Sanjurjo
x-grup: GrupPracitcaC
x-projecte: TRUE
x-company: TRUE
x-foto:< file:/opt/docker/AleixPedraforca.jpg
x-inf:< file:/opt/docker/GrupPracticaC.pdf
```

Per crear la ºimatge, farem la següent ordre:
```bash
docker build -t bryan501/ldap23:practica .
```
Generem la imatge:
```bash
 docker run --rm --name ldap.edt.org -h ldap.edt.org --net 2hisx -p 389:389 -it bryan501/ldap23:practica
```
Generem tambe el phpldapadmin:
```bash
docker run --rm --name php.edt.org -h php.edt.org --net 2hisx -p 80:80 -it bryan501/phpldapadmin23:v2
```
Ens estalviem els dos "docker run":
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
