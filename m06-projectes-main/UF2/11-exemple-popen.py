#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# ------------------------------------

import sys
from subprocess import Popen,PIPE

command =  [ "ls", "/patata", "/opt" ]
pipeData= Popen(command, stdout=PIPE) # Tot el que surt del "who" ho pusa dintra del tub(el pipe)
for line in pipeData.stdout: # Stdout per fer un bucle de cada linea que surt del tub
    print(line.decode("utf-8"), end="")
exit(0)