#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# -------------------------------------
# @ edt ASIX M06 Curs 2022-2023
# Maig 2023
# -------------------------------------
import sys,socket,argparse
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="""ps Client Agent""")
parser.add_argument("server",type=str)
parser.add_argument("-p","--port",type=int, default=50001)
args=parser.parse_args()
HOST = args.server
PORT = args.port
# ---------------------------------------------------------
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
command = "ps ax"
pipeData = Popen(command,shell=True, stdout=PIPE)
for line in pipeData.stdout:
    s.send(line)
s.close()
sys.exit(0)
