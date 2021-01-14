import os

#funcion de validacion de dominios
def validacion (dominio):
    print("En busca del dominio: ", dominio, "dentro del servidor")
    comp_dominio = os.path.isdir("/var/www/vhosts/"+dominio+"/")
    if comp_dominio == True:
        print("Se ah validado y el dominio existe")
        return True
    else:
        print("El dominio no existe en este servidor se procedera a salir")
        return False
