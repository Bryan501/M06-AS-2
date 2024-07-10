Engegar container PAM23:SAMBA
```bash
docker run --rm --name pam.edt.org -h pam.edt.org --net 2hisx --privileged -d bryan501/pam23:samba
```
Accedir al container i comprovar
```bash
docker exec -it pam.edt.org /bin/bash
ps ax
getent passwd
```
Editem el /etc/hosts per tindre connectivitat amb el AWS
```bash
vim /etc/hosts

IP  ldap.edt.org ldap samba.edt.org samba
```
Fem les proves
```bash
smbclient -U pere%pere //samba.edt.org/pere
su - pere
```