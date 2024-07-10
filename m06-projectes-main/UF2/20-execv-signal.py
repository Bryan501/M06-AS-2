#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# signal.py segons
# -------------------------------------
# @edt ASIX M06 Curs 2023-2024
# Abril 2024
# -------------------------------------
import sys, os

print("Hola, començament del programa principal")
print("PID pare:", os.getpid())

pid = os.fork()
if pid != 0:
    # os.wait()
    print("Program pare:", os.getpid(), pid)
    sys.exit(0)

# Programa fill
os.execv("/usr/bin/python3", ["/usr/bin/python3", "16-signal.py", "5"])

print("Hasta luego Diego!")
sys.exit(0)
