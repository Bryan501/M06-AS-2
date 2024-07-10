# Engegar les imatges
```bash
docker compose up -d
```

# Configuració Client

Per configurar el client SSH, es fa ús del fitxer ssh_config, que permet definir opcions específiques per a les connexions sortints des del client. A continuació, es presenten alguns exemples de configuració client amb les seves explicacions:

```bash
# Exemple 1: Habilitar la visualització de claus del servidor
Host *
  VisualHostKey yes
```
Aquesta configuració permet mostrar una representació visual de la clau del servidor quan es connecta. Aquesta opció millora la verificació visual del servidor al moment de la connexió.

...................................................................................................................................................................................................................................................................................................
```bash
# Exemple 2: Establir un límit de temps per a les connexions
Host *
  ConnectTimeout 10
```
En aquest exemple, s'estableix un temps màxim de 10 segons per a la connexió amb els servidors. Això és útil per evitar temps d'espera excessius en connexions que no responen.

...................................................................................................................................................................................................................................................................................................
```bash
# Exemple 3: Configuració per a un host específic
Host servidor1
  HostName servidor1.example.com
  User usuari_ssh
  Port 2022
  PasswordAuthentication no
```
Aquest exemple mostra la configuració específica per al host "servidor1". S'especifica el nom d'usuari, el port i es desactiva l'autenticació per contrasenya.


# Configuració Servidor

La configuració del servidor SSH es realitza mitjançant el fitxer sshd_config. A continuació, es mostren alguns exemples amb explicacions:
```bash
# Exemple 1: Canviar el port SSH per defecte
Port 2022
```
En aquest cas, el servidor escoltarà les connexions SSH al port 2022 en lloc del port predeterminat 22. Això afegirà una capa addicional de seguretat.
...................................................................................................................................................................................................................................................................................................
```bash
# Exemple 2: Desactivar l'accés directe al root
PermitRootLogin no
```
Aquesta configuració impedeix l'accés directe al sistema com a usuari root. És una bona pràctica de seguretat desactivar aquesta opció i utilitzar un usuari normal per iniciar sessió.

...................................................................................................................................................................................................................................................................................................
```bash
# Exemple 3: Restricció d'accés per usuaris específics
AllowUsers usuari1 usuari2
DenyUsers usuari3 usuari4
```
Aquest exemple mostra com permetre l'accés només als usuaris especificats a través d'AllowUsers i com denegar l'accés als usuaris especificats amb DenyUsers.

# Accés SSH per Clau Pública

Per habilitar l'accés SSH utilitzant claus públiques, seguiu aquest procediment:

Generació de claus al client:
```bash
ssh-keygen -t rsa
```
Còpia de la clau al servidor:
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub usuari@servidor
```
Això transferirà la clau pública al servidor i la afegirà al fitxer authorized_keys.

Configuració del client:

Modifiqueu el fitxer ~/.ssh/config al vostre client amb les següents opcions:
```bash
Host servidor
  HostName servidor.example.com
  User usuari
  IdentityFile ~/.ssh/id_rsa
```
Aquesta configuració permetrà accedir al servidor mitjançant una clau pública i evitarà la necessitat de contrasenyes.














