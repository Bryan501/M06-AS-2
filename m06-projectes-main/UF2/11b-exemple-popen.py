#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# program.py ruta
# ------------------------------------

import sys
import argparse
from subprocess import Popen,PIPE


parser = argparse.ArgumentParser( description = "***Mostrar les N primeres lineas***", epilog="that all folks")
parser.add_argument("ruta", type=int, help="Fitxer a processar", metavar="file")
args=parser.parse_args()

command =  [ "ls", args.ruta ]
pipeData= Popen(command, stdout=PIPE) # Tot el que surt del "who" ho pusa dintra del tub(el pipe)
for line in pipeData.stdout: # Stdout per fer un bucle de cada linea que surt del tub
    print(line.decode("utf-8"), end="")
exit(0)