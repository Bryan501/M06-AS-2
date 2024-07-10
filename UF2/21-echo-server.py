#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# M06 Curs 2023-2024
# echo-server.py
# --------------------------------------
import sys,socket
HOST=''
PORT=50001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print("Conn: ", type(conn), conn)
print("Connected by: ", addr) 
while True:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
    print(data)
conn.close()
sys.exit(0)
