#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# popen_sql.py 
# ------------------------------------

import sys
import argparse
from subprocess import Popen,PIPE

# ------------------------------------

parser = argparse.ArgumentParser( description = "***Mostrar les dades d'oficines***")

parser.add_argument("sqlStatement", type=str, help="consulta a la base de dades training")

args=parser.parse_args()

# ------------------------------------

command = "PGPASSWORD=passwd psql -qtA -F ',' -h localhost -U postgres training"

pipeData= Popen(command, shell=True, bufsize=0, universal_newlines=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
pipeData.stdin.write(args.sqlStatement + "\n\q\n")
for line in pipeData.stdout: 
    print(line, end="")
exit(0)
