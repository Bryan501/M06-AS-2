#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# 26-telnet-server-one2one.py [-p port] [-d debug]
# -------------------------------------
# @Bryansito
# ASIX M06 Curs 2024-2025
# Maig 2023
# -------------------------------------

import sys, socket, argparse, signal
from subprocess import Popen, PIPE

parser=argparse.ArgumentParser(description="telnet server")
parser.add_argument("-p","--port", type=int, metavar="port", dest="port", default=50001)
parser.add_argument("-d", "--debug", action="store_true", help="accions")
args=parser.parse_args()

llistapeers=[]

HOST=''
PORT=args.port
DEBUG=args.debug
END=bytes(chr(4),'utf-8')

# -------------------------------

def myusr1(signum, frame):
    print("Signal handler called with signal: ", signum)
    print(llistapeers)
    sys.exit(0)

def myusr2(signum, frame):
    print("Signal handler called with signal: ", signum)
    print(len(llistapeers))
    sys.exit(0)

def myterm(signum, frame):
    print("Signal handler called with signal: ", signum)
    print(llistapeers, len(llistapeers))
    sys.exit(0)

signal.signal(signal.SIGUSR1, myusr1) # 10
signal.signal(signal.SIGUSR2, myusr2) # 12
signal.signal(signal.SIGTERM, myterm) # 15

# ------------------------------

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    llistapeers.append(addr)
    print("Connexió per: ", addr)
    while True:
        ordre = conn.recv(1024)
        if DEBUG: print("Recive", repr(ordre))
        if not ordre: break
        pipeData = Popen(ordre, stdout=PIPE, stderr=PIPE, shell=True)
        for line in pipeData.stdout:
            conn.sendall(line)
            if DEBUG: sys.stderr.write(str(line,'utf-8'))
        for line in pipeData.stderr:
            conn.sendall(line)
            if DEBUG: sys.stderr.write(str(line,'utf-8'))
        conn.sendall(END)
    conn.close()
s.close()
sys.exit(0)
