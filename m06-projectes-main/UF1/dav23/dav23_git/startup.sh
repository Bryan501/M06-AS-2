#! /bin/bash

for user in unix01 unix02 unix03 unix04 unix05
do
  useradd -m -s /bin/bash $user
  echo -e "$user\n$user" | passwd $user
done

mkdir /var/www/webdav
cd /var/www/webdav
git clone https://gitlab.com/edtasixm06/m06-aso.git
cd /opt/docker

a2enmod dav_fs
a2enmod auth_digest

cp apache2-webdav.conf /etc/apache2/conf-enabled
#cp apache2.conf /etc/apache2/apache2.conf
#service apache2 restart
#service apache2 stop
apachectl -DFOREGROUND -k start

