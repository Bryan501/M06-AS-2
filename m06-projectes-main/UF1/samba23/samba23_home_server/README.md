
```bash
docker run --rm --name samba.edt.org -h samba.edt.org --net 2hisx --privileged -d bryan501/samba23:home_server
```
```bash
docker run --rm --name ldap.edt.org -h ldap.edt.org --net 2hisx --privileged -d bryan501/ldap23:latestv2
```

```bash
getent passwd
```

```bash
smbclient -U samba01%samba01 //samba.edt.org/samba01

su - marta
```

## AWS

```bash
chmod 400 keypair-awsm06.pem
ssh -i keypair-awsm06.pem ec2-user@52.44.218.101
sudo yum update
```

Instal·lació docker / docker-compose
```bash
sudo yum install -y yum-utils device-mapper-persistent-data lvm2

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install docker-ce docker-ce-cli containerd.io

sudo yum install docker

sudo systemctl start docker
sudo systemctl enable docker

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

Comprovacions:
docker --version
docker-compose --version
```
```bash
sudo usermod -aG docker ec2-user 
(Sortim i entrem per poder fer les comandes docker sense permisos d’administrador)
```
```bash
docker run --rm --name ldap.edt.org -h ldap.edt.org --net 2hisx --privileged -p 389:389 -d bryan501/ldap23:latestv2

docker run --rm --name samba.edt.org -h samba.edt.org --net 2hisx --privileged -p 445:445 -p 139:139 -d bryan501/samba23:home_server
```
Comprovacions
```bash
docker ps
sudo yum install nmap netstat
nmap localhost
(4 serveis open)

docker exec -it samba.edt.org /bin/bash
smbclient -U pere%pere //samba.edt.org/pere
smb: \> ls
su - pere
```
