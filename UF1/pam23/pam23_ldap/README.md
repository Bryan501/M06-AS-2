
docker run --rm --name pam.edt.org -h pam.edt.org --net 2hisx --privileged -it bryan501/pam23:base

vim /etc/pam.d/chfn:

account optional pam_echo.so [entra al time]
account sufficient pam_time.so debug
account optional pam_echo.so [surt del time]
account required pam_deny.so



/etc/security# vim time.conf:


# Tots els usuaris poden canviar el chfn en l’horari de 8-10
chfn;*;*;Al0800-1000

# Cap usuari pot canviar el chfn en l’horari 8-10.
chfn;*;*;!Al0800-1000

# Tots els usuaris poden canviar el chfn en l’horari de 8-10 i de 16-22.
chfn;*;*;Al0800-1000|Al1600-2200

# L’usuari unix01 pot canviar el finger de 8-14h. Els altres no.
chfn;*;unix01;Al0800-1400

# L'usuari pere només es pot connectar els dies entre setmana (working days)
login;*;pere;Wk

# L’usuaria marta es pot connectar tots els dies per la tarda
login;*;marta;Al1200-2359

/etc/pam.d/chfn:

session optional pam_echo.so [ ara munta directoris ]
session optional pam_mount.so


/etc/security/pam_mount.conf.xml:

# A tots els usuaris es munta dins el seu home un recurs anomenat tmp de 100M corresponent a un ramdisk tmpfs.
<volume user="*" fstype="tmpfs" path="tmp" mountpoint="/home/%(USER)/tmp" size="100M"/>

#Només a l’usuari unix01 es munta dins el seu home un recurs anomenat tmp de 200M corresponent a un ramdisk tmpfs.
<volume user="unix01" fstype="tmpfs" path="tmp" mountpoint="/home/unix01/tmp" size="200M"/>

# A l’usuari unix02 se li munta dins el home un recurs NFS de xarxa. *Nota* Creeu un recurs de xarxa NFS per exemple /usr/share/doc exportat per NFS.
<volume user="unix02" fstype="nfs" server="direccion_del_servidor_NFS" path="/usr/share/doc" mountpoint="/home/unix02/nfs_docs"/>

