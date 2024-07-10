# Configuració del servidor Telnet

## Ports d'entrada

- **Práctica:** 50001
- **SSH:** 22
- **Total:** 0.0.0.0

## Ports de sortida

- **Total:** 0.0.0.0

## Direccio IP Elàstica

- 54.243.234.187

## Scripts i Comandes locals

### Client Telnet (Local)

#### Script: `26-telnet-client-one2one.py`

*[Contingut]*

### Servidor Telnet (AWS)

#### Script: `26-telnet-server-one2one.py`

*[Contingut]*

### Configuració del Servei Telnet en AWS

- Creació del servei:

```shell
sudo -s
cd /etc/systemd/system
```
```shell
vim 2hisxtelnet.service 
```
```shell
[Unit]
Description=Script per gestionarà el servei que actua com un servidor telnet
After=syslog.target network.target

[Service]
WorkingDirectory=/home/admin/
ExecStart=/usr/bin/python3 26-telnet-server-one2one.py
Restart=always
RestartSec=129

[Install]
WantedBy=multi-user.target
```

- Recargar el sistema:
```shell
systemctl daemon-reload
```
- Gestió del servei
```shell
systemctl start 2hisxtelnet.service 
systemctl stop 2hisxtelnet.service 
systemctl reload 2hisxtelnet.service 
systemctl status 2hisxtelnet.service 
```
# Operacions i comandes

## AWS

- Executar el servidor Telnet:
```shell
python3 26-telnet-server-one2one.py 
```

## LOCAL

- Executar el client Telnet:
```shell
python3 26-telnet-client-one2one.py -s 54.243.234.187 -p 50001
```
- Comandes locals:
```shell
ls
pwd
id
bye  (para salir)
```
## AWS
- Ver registres del servei Telnet:
```shell
journalctl -xeu 2hisxtelnet.service 
```
- Aturar el servidor Telnet:
```shell
sudo pkill python3
```
- Ver el PID del proces del servidor Telnet:
```shell
sudo pgrep python3
```
## Mapeo
- Verificació dels ports:
```shell
nmap localhost
netstat -tulp
ss -lt
```
- Veure el procés del servidor Telnet:
```shell
ps ax | grep "python3 26-telnet-server-one2one.py"
```
- Enviar señal de control al servidor Telnet (por exemple, SIGUSR1):
```shell

kill -10 1339

Connexió per: ('95.17.62.23', 58436)
Connexió per: ('95.17.62.23', 58444)
Connexió per: ('95.17.62.23', 58452)
Connexió per: ('95.17.62.23', 58454)
```
- Enviar otra señal de control al servidor Telnet (por exemple, SIGUSR2):
```shell
kill -12 1339

Connexió per:  ('95.17.62.23', 55718)
Connexió per:  ('95.17.62.23', 55726)
Signal handler called with signal:  12
2
```
- Enviar una señal de terminación al servidor Telnet (por exemple, SIGTERM):
```shell

kill -15 1339

Connexió per:  ('95.17.62.23', 38646)
Connexió per:  ('95.17.62.23', 38656)
Signal handler called with signal:  15
[('95.17.62.23', 38646), ('95.17.62.23', 38656)] 2
```