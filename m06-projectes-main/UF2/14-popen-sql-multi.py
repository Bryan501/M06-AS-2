#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# popen_sql.py -c num_cli -c num_cli
# ------------------------------------

import sys
import argparse
from subprocess import Popen,PIPE

# ---------------------------------------------------------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser( description = "***Mostrar les dades d'oficines***")

parser.add_argument("-c", "--num-clie", type=str, action="append", help="Num de clients", dest="num_clie", required=True)

args = parser.parse_args()

# ---------------------------------------------------------------------------------------------------------------------------------------------

command = "PGPASSWORD=passwd psql -qtA -F ',' -h localhost -U postgres training"

pipeData= Popen(command, shell=True, bufsize=0, universal_newlines=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)

for clients in args.num_clie:
    sqlStatement="select * from clientes where num_clie=%s;" % ( clients )
    pipeData.stdin.write(sqlStatement+"\n")
    print(pipeData.stdout.readline(), end="")
    
pipeData.stdin.write("\q\n")
exit(0)

