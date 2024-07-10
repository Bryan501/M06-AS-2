# /usr/bin/python3
#-*- coding: utf-8-*-
#
# telnet-client.py [-p port] server
# -------------------------------------
# @ edt ASIX M06 Curs 2022-2023
# Maig 2023
# -------------------------------------
# 26-telnet-client-one2one.py -p port -s server
# 26-telnet-server-one2one.py [-p port] [-d debug]
# Implementar un servidor i un client telnet. Client i server fan un diàleg.
# Cal un senyal de “yatà” Usem chr(4).
# Si s’indica debug el server genera per stdout la traça de cada connexió.

# ---------------------------------------------------------

import sys,socket
from subprocess import Popen, PIPE
import argparse

# ---------------------------------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, dest="port", metavar="port", help="port del server", required=True)
parser.add_argument("-s", "--server", type=str, required=True, metavar="server", help="ip/host del servidor")
args=parser.parse_args()

# ---------------------------------------------------------

HOST = args.server
PORT = args.port
MYEOF = bytes(chr(4), 'utf-8')
CM_EXIT = "bye"

# -------------------------------------------------------------

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))

while True:
    command = input("bryan$ ")
    if command.lower() == CM_EXIT: break    
    s.sendall(bytes(command, 'utf-8'))    
    while True:
        data = s.recv(1024)
        if data[-1:] == MYEOF: 
            print(str(data[:-1]))
            break
        print(str(data))
s.close()
sys.exit(0)
