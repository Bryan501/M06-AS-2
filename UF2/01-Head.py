#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# ------------------------------------

import sys 

MAX = 5

fileIn = sys.stdin          # Per defecte processare un fluxe stdin

if len(sys.argv) == 2:
    fileIn = open(sys.argv[1], "r")

cont = 0

for line in fileIn:
    cont += 1
    print(line,end="")

    if cont == MAX: break

fileIn.close()
exit(0)
