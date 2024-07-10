#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# head [ -n 5|10|15 ] [ -f file ] ...
#   default=10, file o stdin
#
#  python3 04-headchoices.py -n 5 -f dades.txt
# ------------------------------------
import sys
import argparse

parser = argparse.ArgumentParser( description = "***Mostrar les N primeres lineas***", epilog="that all folks")
parser.add_argument("-n", "--nlin", type=int, choices=[5, 10, 15], help="Numero lineas (5, 10, o 15)", dest="nlin", metavar="num_lines", default=10)
parser.add_argument("-f", "--fit", type=str, help="Fitxer a processar (stdin)", dest="fileList", metavar="file", action="append")

args = parser.parse_args()
print(args)

# ----------------------------------------------------------------------------------------------------------

MAX = args.nlin


def headFile(fitxer):
    fileIn = open(fitxer, "r")
    cont = 0

    for line in fileIn:
        cont += 1
        print(line,end="")

        if cont == MAX: break

    fileIn.close()

for fileName in args.fileList:
    headFile(fileName)

exit(0)