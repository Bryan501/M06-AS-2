#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# head [ -n 5|10|15 ] file 
# default=10, file o stdin
#
#  python3 04-headchoices.py -n 5 -f dades.txt
# ------------------------------------

import sys
import argparse

parser = argparse.ArgumentParser(description="Mostrar las N primeras líneas", epilog="Eso es todo, amigos")
parser.add_argument("-n", "--nlin", type=int, choices=[5, 10, 15], help="Número de líneas (5, 10 o 15)", dest="nlin", metavar="num_lines", default=10)
parser.add_argument("fitxer", type=str, help="Archivo a procesar (stdin)", metavar="file")

args = parser.parse_args()
print(args)

# ------------------------------------
MAX = args.nlin

fileIn = open(args.fitxer, "r")

cont = 0

for line in fileIn:
    cont += 1
    print(line,end="")

    if cont == MAX: break

fileIn.close()
exit(0)


