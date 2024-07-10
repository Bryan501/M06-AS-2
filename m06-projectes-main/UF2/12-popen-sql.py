#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# popen_sql.py 
# ------------------------------------

import sys
import argparse
from subprocess import Popen,PIPE


parser = argparse.ArgumentParser( description = "***Mostrar les dades d'oficines***", epilog="that all folks")
args=parser.parse_args()

command = ["psql", "-qtA", "-F','", "-h", "localhost", "-U", "postgres", "training", "-c", "select * from oficinas;"]
pipeData= Popen(command, stdout=PIPE) # Tot el que surt del "who" ho pusa dintra del tub(el pipe)
for line in pipeData.stdout: # Stdout per fer un bucle de cada linea que surt del tub
    print(line.decode("utf-8"), end="")
exit(0)