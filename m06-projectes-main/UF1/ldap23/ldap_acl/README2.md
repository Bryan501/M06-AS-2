# engegar el container:
docker run --rm --name mi-ldap -h ldap.edt.org --net 2hisx -p 389:389 -d bryan501/acl23:latest
# llista la base de dades 1:
ldapsearch -x -LLL -D 'cn=Sysadmin,cn=config' -w syskey -b 'olcDatabase={1}mdb,cn=config'
# atributs
ldapsearch -x -LLL -D 'cn=Sysadmin,cn=config' -w syskey -b 'olcDatabase={1}mdb,cn=config' olcAcces
# afegir
ldapmodify -vx -D 'cn=Sysadmin,cn=config' -w syskey -f acl1.ldif

##############################################
# editar el ldap.conf
vim /etc/ldap/ldap.conf 


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
URI ldap://ldap.edt.org



########################################## 

ldapsearch -x -LLL mail

ldapsearch -x -LLL -D "cn=Anna Pou,ou=usuaris,dc=edt,dc=org" -w anna  dn mail

# no deixa mdoificar altres usuairs, ni al teu propi usuari. Pero Manager sí
ldapmodify -vx -D "cn=Anna Pou,ou=usuaris,dc=edt,dc=org" -w anna -f mod1.ldif

# ldapmodify -x -D "cn=Sysadmin,cn=config" -w syskey -f acl-e2.ldif 


#credentials = password malament
