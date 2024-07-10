#! /bin/bash

for user in unix01 unix02 unix03 unix04 unix05
do
  useradd -m -s /bin/bash $user
  echo -e "$user\n$user" | passwd $user
done

/usr/sbin/nslcd
/usr/sbin/nscd

# Share public
mkdir /var/lib/samba/public
chmod 777 /var/lib/samba/public
cp /opt/docker/* /var/lib/samba/public/.

# Share privat
mkdir /var/lib/samba/privat
# chmod 777 /var/lib/samba/privat
cp /etc/os-release /var/lib/samba/privat/.

# Copiar la configuració
cp /opt/docker/smb.conf /etc/samba/smb.conf

# Creació usuaris unix/samba
for user in samba01 samba02 samba03 samba04 samba05
do
  useradd -m -s /bin/bash $user
  echo -e "$user\n$user" | smbpasswd -a $user
done

chmod +x /opt/docker/usersldap.sh
bash /opt/docker/usersldap.sh

# Activar els serveis
/usr/sbin/smbd && echo "smb Ok"
/usr/sbin/nmbd -F && echo "nmb  Ok"

sleep infinity


