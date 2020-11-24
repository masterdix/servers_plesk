import os

def validacion (dominio):
    print("En busca del dominio: ", dominio, "dentro del servidor")
    os.system("cd /var/www/vhost")
    comp_dominio = os.path.isdir(dominio)
    if comp_dominio == True:
        print("Se ah validado y el dominio existe")
        return True
    else:
        print("El dominio no existe en este servidor se procedera a salir")
        return False