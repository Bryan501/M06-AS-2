# /usr/bin/python3
#-*- coding: utf-8-*-
#
# signal-exemple.py
# -------------------------------------
# @ edt ASIX M06 Curs 2023-2024
# Abril 2024
# -------------------------------------
import sys, os, signal

def myhandler(signum, frame):
    print("Signal handler with signal: ", signum)
    print("hasta luego lucas!")
    sys.exit(0)

def nodeath(signum, frame):
    print("Signal handler with sifgnal:, signum")
    print("Tururut! more't tu!")

# Assignar un handler al senyal
signal.signal(signal.SIGUSR1,myhandler)       #10
signal.signal(signal.SIGUSR2,nodeath)         #12
signal.signal(signal.SIGALRM,myhandler)       #14
signal.signal(signal.SIGTERM,signal.SIG_IGN)  #15
signal.signal(signal.SIGINT,signal.SIG_IGN)   #2

signal.alarm(60)
print(os.getpid())
while True:
    pass    
sys.exit(0)
