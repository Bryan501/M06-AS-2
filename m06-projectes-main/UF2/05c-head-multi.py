#! /usr/bin/python3
#-*- coding: utf-8-*-
# @edt ASIX M06 Curs 2024-2025
# head [ -n 5|10|15 ] file -v ...
#   default=10
#
#  python3 04-headchoices.py -n 5 -f dades.txt
# ------------------------------------
import sys
import argparse

parser = argparse.ArgumentParser( description = "***Mostrar les N primeres lineas***", epilog="that all folks")
parser.add_argument("-n", "--nlin", type=int, choices=[5, 10, 15], help="Numero lineas (5, 10, o 15)", dest="nlin", metavar="num_lines", default=10)
parser.add_argument("fileList", help="Archivo a procesar (stdin)", metavar="file", nargs="+")
parser.add_argument("-v", "--verbose", action="store_true")

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

if args.fileList:
    for fileName in args.fileList:
        if args.verbose:
            print("\n",fileName)
        headFile(fileName)

sys.exit(0)