import os
import order.day0
import earth
#funcion de validacion de dominios
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

def menu_resp (dominio):
    order.day0.submenu_resp()
    select = input("Que operacion desea realizar:  ")
    if select == 1:
        earth.validacion_respaldo(dominio)
    