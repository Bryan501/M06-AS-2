#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# signal.py segons
# -------------------------------------
# @edt ASIX M06 Curs 2023-2024
# Abril 2024
# -------------------------------------
import sys,os
print("Hola, començament del programa principal")
print( "PID pare: ", os.getpid())

pid=os.fork()
if pid != 0:
    #os.wait()
    print("Program pare: ", os.getpid(), pid)
else:
    print("Program fill: ", os.getpid(), pid)
    while True:
        pass
print("Hasta luego Diego!")
sys.exit(0)