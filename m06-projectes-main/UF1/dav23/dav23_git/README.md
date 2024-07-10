Entrem d'ins del pam:
```bash
docker exec -it pam.edt.org /bin/bash
```

Iniciem sessió amb un usuari local. Veurem que es crea al home del usuari "mytmp":
```bash
root@pem:/opt/docker# su - unix01
reenter password for pam_mount:
unix01@pem:~$ ls
mytmp
```
Fem lo mateix pero amb un usuari LDAP. Veurem que es crea al home del usuari "apunts", amb els apunts/carpeta "m06":

```bash
unix01@pem:~$ su - pere
Password: 
Creating directory '/tmp/home/pere'.
$ ls
apunts
$ ls apunts
lost+found  m06-aso
```

També podem comprovar que s'hi hagi clonat els apunts de m06 per google:
```html
http://localhost/webdav
```
