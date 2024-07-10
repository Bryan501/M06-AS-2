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
print( "PID pare: ", os.getpid())

pid=os.fork()
if pid != 0:
    #os.wait()
    print("Program pare: ", os.getpid(), pid)
    sys.exit(0)

# Programa fill

#os.execv("/usr/bin/ls", ["/usr/bin/ls", "-la", "/"])
#os.execl("/usr/bin/ls","/usr/bin/ls","-la","/")
#os.execlp("ls","ls","-la","/")
#os.execvp("uname", ["uname", "-a"])
#os.execl("/bin/bash", "/bin/bash","show.sh") #nom="pere" edat="15" python3 19-exemple-execv.py
os.execvpe("/bin/bash", ["/bin/bash", "show.sh"], {"nom":"joan","edat":"25"})

print("Hasta luego Diego!")
sys.exit(0)
