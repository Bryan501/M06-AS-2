#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# head [ -n nlin ] [ -f file ]
#   default=10, file o stdin
# ------------------------------------
import sys, argparse

parser = argparse.ArgumentParser( description = "***Mostrar les N primeres lineas***", epilog="that all folks")
parser.add_argument("-n", "--nlin", type=int, help="Numero lineas", dest="nlin", metavar="num_lines", default=10)
parser.add_argument("-f", "--fit", type=str, help="Fitxer a processar (stdin)", dest="fitxer", metavar="file", default="dev/stdin")


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

