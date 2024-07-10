#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# server01.py [-p port] [-d debug]
# provar-ho: nc localhost 44444
# -------------------------------------
# @Bryansito
# ASIX M06 Curs 2024-2025
# Maig 2023
# -------------------------------------

import argparse, sys, socket, os, signal
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser()
parser.add_argument("-p","--port", type=int, dest="port", metavar="port", help="Server's port", default=44444)
parser.add_argument("-d","--debug", action="store_true", help="Keep trace of the server")
args = parser.parse_args()

HOST = ''
PORT = args.port
DEBUG = args.debug
EOF = bytes(chr(4),'utf-8')
CM_EXIT = "bye"

llista_peer = []

# --------------------------------------------

def show_peers(signum, frame):
    global llista_peer
    print("Connected peers:")
    for peer in llista_peer:
        print(peer)
    s.close()
    sys.exit(0)

def peer_count(signum, frame):
    global llista_peer
    contador = 0
    for peer in llista_peer:
        contador += 1
    print("Total of connections:", contador)
    s.close()
    sys.exit(0)

def show_all(signum, frame):
    global llista_peer
    contador = 0
    print("Connected peers:")
    for peer in llista_peer:
        contador += 1
        print(peer)
    print("Total of connections:", contador)
    s.close()
    sys.exit(0)

# --------------------------------------------

pid=os.fork()
if pid != 0:
    print("Servei engegat")
    sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

signal.signal(signal.SIGUSR1, show_peers) # 10
signal.signal(signal.SIGUSR2, peer_count) # 12
signal.signal(signal.SIGTERM, show_all)   # 15

s.bind((HOST,PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    llista_peer.append(addr)
    print(addr)
    while True:
        command = conn.recv(1024)
        if DEBUG:
            print("Received:", repr(command))
        if not command: break
        command_linux = command.decode().strip() 
        if command_linux == 'processos':
            linux_com = "ps ax"
        elif command_linux == 'ports':
            linux_com = "ss -pta"
        elif command_linux == 'bye':
            conn.close() 
            break
        else:
            linux_com = "uname -a"
        if DEBUG:
            print("Sending:", linux_com)
        pipeData = Popen(linux_com, stdout=PIPE, shell=True)
        for line in pipeData.stdout:
            conn.sendall(line)
        conn.sendall(EOF)
    conn.close()
s.close()
sys.exit(0)  

