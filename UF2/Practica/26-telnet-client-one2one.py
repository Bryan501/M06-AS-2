#! /usr/bin/python3
#-*- coding: utf-8-*-
#
# 26-telnet-client-one2one.py [-p port] [-s server]
# -------------------------------------
# @Bryansito
# ASIX M06 Curs 2024-2025
# Maig 2023
# -------------------------------------

import sys,socket, argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, dest="port", metavar="port", help="port del server", required=True)
parser.add_argument("-s", "--server", type=str, dest="server", metavar="server", help="ip/host del servidor", required=True)
args=parser.parse_args()

HOST = args.server
PORT = args.port
END = bytes(chr(4),'utf-8')
CM_EXIT = "bye"

# -------------------------------------------------------------

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST,PORT))

while True:
  command = input("bryan$ ")
  if command.lower() == CM_EXIT: break  
  s.sendall(bytes(command, 'utf-8'))  
  while True:
      data = s.recv(1024)
      if data[-1:] == END:
          print(data[:-1].decode())
          break
      print((data).decode().strip())
s.close()
sys.exit(0)