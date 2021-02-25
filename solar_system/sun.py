import os
from chaos import bcolors

#funcion de validacion de dominios
def validacion (dominio):
    print(bcolors.yellow, "En busca del dominio: ", dominio, "dentro del servidor", bcolors.endc)
    comp_dominio = os.path.isdir("/var/www/vhosts/"+dominio+"/")
    if comp_dominio == True:
        print(bcolors.green, "Se ah validado y el dominio existe", bcolors.endc)
        return True
    else:
        print(bcolors.red, "El dominio no existe en este servidor se procedera a salir", bcolors.endc)
        return False
