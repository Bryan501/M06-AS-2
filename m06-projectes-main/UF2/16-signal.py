#! /usr/bin/python3
#-*- coding: utf-8 -*-
# 
# M06 Curs 2023-2024
# singla-exemple.py
# --------------------------------------
import sys, os, signal, argparse
parser = argparse.ArgumentParser(description="Gestionar alarma")
parser.add_argument("segons", type=int,\
        help="segons")
args=parser.parse_args()
#print(args)
#exit(0)

up=0
down=0

def usr1(signum, frame):
    print("Signal handler with signal: ", signum)
    global up
    actual=signal.alarm(0)
    signal.alarm(actual+60)
    up+=1

def usr2(signum, frame):
    print("Signal handler with signal: ", signum)
    global down
    actual=signal.alarm(0)
    if actual > 60:
        signal.alarm(actual-20)
    else:
        print("No és pot restar, segons que queden: ",actual)
        signal.alarm(actual)
    down+=1

def myalarm(signum, frame):
    print("Signal handler called with signal:", signum)
    print("Finalitzant... up: %d down:%d restant: %d" % (up, down, signal.alarm(0)))
    sys.exit(0)

def myterm(signum,frame):
    print("Signal handler called with signal:", signum)
    actual = signal.alarm(0)
    signal.alarm(actual)
    print("Temps restant: ", actual)

def myhup(signum,frame):
    print("Signal handler called with signal:", signum)
    print("Temps restaurat, valor: ", args.segons)
    signal.alarm(args.segons)

# Assignar un handler al senyal
signal.signal(signal.SIGUSR1,usr1)          #10
signal.signal(signal.SIGUSR2,usr2)          #12
signal.signal(signal.SIGALRM,myalarm)         #14
signal.signal(signal.SIGTERM,myterm)          #15
signal.signal(signal.SIGHUP,myhup)            #1
signal.signal(signal.SIGINT,signal.SIG_IGN)   #2

signal.alarm(args.segons)

print(os.getpid())
while True:
    pass
sys.exit(0)
