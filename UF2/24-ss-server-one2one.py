#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# M06 Curs 2023-2024
# daytime-server.py
# --------------------------------------
import sys, socket, argparse, signal, os
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="""ss server""")
parser.add_argument("-p","--port",type=int, default=50001)
args=parser.parse_args()
HOST = ''
PORT = args.port
llistaPeers=[]
#-------------------------------------
def myusr1(signum, frame):
    print("Signal handler with signal: ", signum)
    print(llistaPeers)
    sys.exit(0)

def myusr2(signum, frame):
    print("Signal handler wih signal: ", signum)
    print(len(llistaPeers))
    sys.exit(0)

def myterm(signum, frame):
    print("Sginal handler with signal: ", signum)
    print(llistaPeers, len(llistaPeers))
    sys.exit(0)

pid=os.fork()
if pid != 0:
    print("Engegat el server ss", pid)
    sys.exit(0)
signal.signal(signal.SIGUSR1,myusr1)          #10
signal.signal(signal.SIGUSR2,myusr2)          #12
signal.signal(signal.SIGTERM,myterm)          #15


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    print("Connected by", addr)
    llistaPeers.append(addr)
    command = "ss -ltn"
    pipeData = Popen(command,stdout=PIPE)
    for line in pipeData.stdout:
        conn.send(line)
    conn.close()
