#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# M06 Curs 2023-2024
# daytime-server.py
# --------------------------------------
import sys, socket, argparse
from subprocess import Popen, PIPE
parser=argparse.ArgumentParser(description="""Client""")
parser.add_argument("-s","--server",type=str, default='')
parser.add_argument("-p","--port", type=int, default=50001)
args=parser.parse_args()
HOST=args.server
PORT=args.port

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


