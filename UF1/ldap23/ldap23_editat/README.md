# Imatge personalitzada de Debian per utilizar LDAP en mode detach

Aquesta imatge de Docker està basada en un Debian i conté el procés de com instal·lar el servei
LDAP i mitjançant això navegar per les dades que hi posarem. I també editar el contigut de fitxers.

## Dockerfile

L'arxiu "Dockerfile" definirà els passos a seguir per a la construcció de l'imatge Docker.

## Startup.sh

L'arxiu "Startup.sh" s'executarà mitjançant el "Dockerfile" sense necesitat de fer totes les comandes
des d'adins del container. On farem els següents passos a seguir:

1-Esborrar els directoris de configuració i de dades.
2-Generar el directori de configuració dinàmica slapd.d a partir del fitxer de configuració slapd.conf.
3-Injectar a baix nivell les dades de la BD 'populate' de l'organització dc=edt,dc=org.
4-Assignar la propietat i grup del directori de ddaes i de configuració a l'usuari openldap.
5-Engegar el servei slapd amb el paràmetre que fa debug per mantenir-lo engegat en foreground.

## edt-org.ldif

L'arxiu "edt-org.ldif" tindrà les entitats que volem on  s'utilitzarà mitjançant el "startup.sh" per agafar les nostres entitats (les dades) i substituir-les per les de defecte. Amb nous usuaris (user0-11) i un nous grups.

## slapd.conf

L'arxiu "slapd.conf" tindrà la nostra configuració que volem al LDAP.

## Desenvolupament

Passos a realitzar el desenvolupament:

-Generar un sol fitxer ldif anomenat edt-org.ldif (usuaris0-11):
-   Dins del fitxer edt-org.ldif farem la creació de nous usuaris del 0 al 11 amb el seu contingut propi i una ou.

-Afegir en el fitxer dos usuaris i una ou nova inventada i     posar-los dins la nova ou:
-   A més a més, ficarem dos usuaris més inventats amb un grup inventat per a ells.

-Modificar el fitxer edt-org.ldif modificant dn dels usuaris utilitzant en lloc del cn el uid per identificar-los (rdn):
-   Manualment editarem el fitxer "edt-org.ldif" on els dos nous usuaris inventats tindran el cn remplaçat per uid

-Configurar el password de Manager que sigui ‘secret’ però encriptat (posar-hi un comentari per indicar quin és de cara a estudiar):
-   Ens ficarem al fitxer de configuració "slapd.conf" on al rootpw ficarem la password secret de manera enctiptada, mitjançant la comanda "slappasswd" i documentarem el   rootpw anterior per sapiguer quina password era.

-Propagar el port amb -p -P
-   Farem la propagació de port fent la comanda "-p 389:389" que 389 seria per propagar el port del LDAP

-Editar els dos README, en el general afegir que tenim una nova imatge. En el de la imatge ldap22:editat
-   Explicarem mitjançant el README.md tot el desenvolupament que estem fent ara.

-Descriure els canvis i les ordres per posar-lo en marxa.
-   Basicament al abans redactat.

-Configurar la base de dades cn=config amb un usuari administrador anomenat syadmin i password syskey.
-   Dins del fitxer "slapd.conf" crear una nova base de dades apart anomenat config, on l'admin sigui sysadmin i de password syskey.

-Verifiqueu que sou capaços de modificar la configuració de la base de dades edt.org en calent modificant per exemple el passwd o el nom o els permisos.
-   Comprovacions.

Per crear la ºimatge, farem la següent ordre:
```bash
docker build -t bryan501/ldap23:editat .
```
Generem la imatge en mode interactiu per veure que passa al fer "docker run" i ficarem la propagasio de ports:
```bash
docker run --rm --name mi-ldap -h ldap.edt.org -p 389:389 -it bryan501/ldap23:editat
```
Farem la comprovació de que ens deixa modificar els usuaris del "edt-org.ldif" i comprovem:
```bash
docker exec -it mi-ldap ldapmodify -x -D "cn=Manager,dc=edt,dc=org" -w secret -f mod.ldif
docker exec -it mi-ldap ldapsearch -x -D "cn=Manager,dc=edt,dc=org" -w secret -b "dc=edt,dc=org" "uidNumber=5030"
docker exec -it mi-ldap slapcat
```



