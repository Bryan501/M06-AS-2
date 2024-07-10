#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# signal.py segons
# -------------------------------------
# @edt ASIX M06 Curs 2023-2024
# Abril 2024
# -------------------------------------

import sys
import os
import signal

def hola(signum, frame):
    print("Signal handler called with signal:", signum)
    print("Hola!")

def adeu(signum, frame):
    print("Signal handler called with signal:", frame)
    print("Adeu!")
    sys.exit(0)

print("Hola, començament del programa principal")
print( "PID pare: ", os.getpid())

pid=os.fork()

if pid != 0:
    print("Program pare: ", os.getpid(), pid)
    print("Llançat el procés fill servidor")
    sys.exit(0)

print("Program fill: ", os.getpid(), pid)
signal.signal(signal.SIGUSR1, hola)
signal.signal(signal.SIGUSR2, adeu)
while True:
    pass
