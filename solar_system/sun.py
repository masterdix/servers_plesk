import os
from order.day0 import bcolors

#Función de Validación de dominios
#Se encarga de validar si existe el directorio, para poder trabajar con el
#si este no existe, entrega un false para salir del progrma.
def validacion (dominio):
    print(bcolors.yellow)
    print("En busca del dominio: ", dominio, "dentro del servidor")
    print(bcolors.endc)
    
    #--Variables de almacenamiento--
    comp_dominio = os.path.isdir("/var/www/vhosts/"+dominio+"/")
    
    comp_mailing= os.path.isdir("/var/qmail/mailnames/"+dominio+"/")
    
    #--Validación de carpeta de hosting--
    if comp_dominio == True:
        print(bcolors.green)
        print("Se ah validado y el dominio existe")
        print(bcolors.endc)
        return True
    
    #--Validación de carpeta de correos--
    elif comp_mailing == True:
        print(bcolors.green)
        print("Se ah validado y el dominio existe")
        print(bcolors.endc)
        return True
    
    #--Negativa--
    else:
        print(bcolors.red)
        print("El dominio no existe en este servidor se procedera a salir")
        print(bcolors.endc)
        return False
