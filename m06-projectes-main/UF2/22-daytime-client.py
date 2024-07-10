#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# M06 Curs 2023-2024
# daytime-server.py
# --------------------------------------
import sys, socket
from subprocess import Popen, PIPE
HOST=''
PORT=50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUDEADDR,1)
s.connect((HOST,PORT))
# bucle
while True: 
    data= s.recv(1024)
    if not data: break
    print("Data: ", repr(data))
s.close()
sys.exit(0)

