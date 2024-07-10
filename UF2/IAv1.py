#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse

parser = argparse.ArgumentParser(description="***Mostrar les N primeres líneas***", epilog="Eso es todo, amigos")
parser.add_argument("-n", "--nlin", type=int, choices=[5, 10, 15], help="Número de líneas (5, 10 o 15)", dest="nlin", metavar="num_lines", default=10)
parser.add_argument("-f", "--fit", type=str, help="Archivo(s) a procesar (stdin)", dest="fitxer", metavar="file", default=[], action="append")

args = parser.parse_args()

MAX = args.nlin

for file in args.fitxer:
    with open(file, "r") as fileIn:
        cont = 0
        for line in fileIn:
            cont += 1
            print(line, end="")
            if cont == MAX:
                break

sys.exit(0)
