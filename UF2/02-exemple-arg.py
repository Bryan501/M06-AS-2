#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(
    description="programa de ejemplo de argumentos",
    prog="02-arguments.py",
    epilog="¡Hasta luego MariCarmen!")

parser.add_argument("-n", "--nom", type=str, help="nom usuari")
parser.add_argument("-e", "--edat", type=int, dest="userEdat", help="edat a prcoessar", metavar="edat")

args = parser.parse_args()
print(args)
print(args.userEdat, args.nom)
exit(0)

# python3 02-exemple-arg.py -h 
# python3 02-exemple-arg.py -n patata
# python3 02-exemple-arg.py --nom patata
# python3 02-exemple-arg.py -n patata -e 12
# help(l)
# help(num)  mostra l'ajuda
# dir(nom)


