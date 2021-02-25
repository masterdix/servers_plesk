import os
from order.day0 import bcolors

#funcion de validacion de dominios
def validacion (dominio):
    print(bcolors.yellow)
    print("En busca del dominio: ", dominio, "dentro del servidor")
    print(bcolors.endc)
    comp_dominio = os.path.isdir("/var/www/vhosts/"+dominio+"/")
    if comp_dominio == True:
        print(bcolors.green)
        print("Se ah validado y el dominio existe")
        print(bcolors.endc)
        return True
    else:
        print(bcolors.red)
        print("El dominio no existe en este servidor se procedera a salir")
        print(bcolors.endc)
        return False
