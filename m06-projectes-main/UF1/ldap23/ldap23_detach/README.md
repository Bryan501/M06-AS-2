# Imatge personalitzada de Debian per utilizar LDAP en mode detach

Aquesta imatge de Docker està basada en un Debian i conté el procés de com instal·lar el servei
LDAP i mitjançant això navegar per les dades, que hi posarem, fora del contenidor.

## Dockerfile

L'arxiu "Dockerfile" definirà els passos a seguir per a la construcció de l'imatge Docker.

## Startup.sh

L'arxiu "Startup.sh" s'executarà mitjançant el "Dockerfile" sense necesitat de fer totes les comandes
des d'adins del container. On farem els següents passos a seguir:

1) Esborrar els directoris de configuració i de dades.
2) Generar el directori de configuració dinàmica slapd.d a partir del fitxer de configuració slapd.conf.
3) Injectar a baix nivell les dades de la BD 'populate' de l'organització dc=edt,dc=org.
4) Assignar la propietat i grup del directori de ddaes i de configuració a l'usuari openldap.
5) Engegar el servei slapd amb el paràmetre que fa debug per mantenir-lo engegat en foreground.

## edt-org.ldif

L'arxiu "edt-org.ldif" tindrà les entitats que volem on  s'utilitzarà mitjançant el "Startup.sh" 
per agafar les nostres entitats (les dades) i substituir-les per les de defecte.

## slapd.conf

L'arxiu "slapd.conf" tindrà la nostra configuració que volem al LDAP.

## Desenvolupament

Per crear la ºimatge, farem la següent ordre:
```bash
docker build -t bryan501/ldap23:detach .
```
Generem la imatge en mode detach (ficarem el -p per connectar els ports del sistema remot amb el local):
```bash
docker run --rm --name mi-ldap -h ldap.edt.org -p 389:389 -d bryan501/ldap23:detach
```
Podem comprovar en el nostre sistema local si el port està sent utilitzat, per quin servei i una vegada
hem comprovat, fer comandes per verificar si podem buscar informació en el Docker:
```bash
# Busca i mostra les connexions que estan escoltant el port 389:

sudo netstat -tuln | grep "389"

# Busca i mostra els serveis que estan utilitzant el port 389:

sudo lsof -i :389 | grep "LISTEN"

# Verifiquem que podem buscar entitats:

ldapsearch -x -LLL -b 'dc=edt,dc=org'
ldapsearch -x -LLL -b 'dc=edt,dc=org' dn
ldapsearch -x -LLL -b 'dc=edt,dc=org' cn mail
ldapsearch -x -LLL -b 'ou=usuaris,dc=edt,dc=org' cn mai
ldapsearch -x -LLL -H ldap://172.17.0.2 -b 'dc=edt,dc=org' | grep dn
```

