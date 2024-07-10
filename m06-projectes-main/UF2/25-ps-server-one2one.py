#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# -------------------------------------
# @ edt ASIX M06 Curs 2022-2023
# Maig 2023
# -------------------------------------
import sys, socket, argparse, signal, os, time
from subprocess import Popen, PIPE
from datetime import datetime
parser = argparse.ArgumentParser(description="""ps server""")
parser.add_argument("-p","--port", type=int, default=50001)
args = parser.parse_args()
HOST = ''
PORT = args.port
llistapeers=[]
# ---------------------------------

def myusr1(signum, frame):
    print("Signal handler with signal: ", signum)
    print(llistapeers)
    sys.exit(0)

def myusr2(signum, frame):
    print("Signal handler wih signal: ", signum)
    print(len(llistapeers))
    sys.exit(0)

def myterm(signum, frame):
    print("Sginal handler with signal: ", signum)
    print(llistapeers, len(llistapeers))
    sys.exit(0)

pid=os.fork()
if pid != 0:
    print("Engegat el server ps", pid)
    sys.exit(0)
signal.signal(signal.SIGUSR1,myusr1)          #10
signal.signal(signal.SIGUSR2,myusr2)          #12
signal.signal(signal.SIGTERM,myterm)          #15

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(1)
# bucle per cada client
while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    sys.stdout.flush()
    llistapeers.append(addr)
    command="ps ax"
    fitxer = "/tmp/%s-%s-%s.log"%(addr[0], addr[1], time.strftime("%Y%m%d-%H%M%s"))
    # obrir
    fitxer = open(fitxer, "w")
    while True:
        data = conn.recv(1024)
        if not data: break
        fitxer.write(str(data))
    conn.close()
    fitxer.close()
