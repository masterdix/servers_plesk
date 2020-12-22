import os
import order.day0
import solar_system.earth
import chaos
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
#Submenu respaldo
def menu_resp (dominio):
    order.day0.submenu_resp()
    select = input("Que operacion desea realizar:  ")
    #validacion de existencia de respaldo
    if select == 1:
        solar_system.earth.validacion_respaldo(dominio)
    #borrado de respaldo web
    if select == 2:
        print("desactivado por proteccion")
        menu_resp(dominio)
    #borrado de respaldo mail
    if select == 3:
        print("desactivado por proteccion")
        menu_resp(dominio)
    #creacion de respaldo web
    if select == 4:
        solar_system.earth.crear_respaldo_web(dominio)
    #creacion de respaldo mail
    if select == 5:
        solar_system.earth.crear_respaldo_qmail(dominio)
    #subir respaldo web
    if select == 6:
        solar_system.earth.sync_web(dominio)
    #subir respaldo correo
    if select == 7:
        solar_system.earth.sync_mail(dominio)
    #regresa al menu principal
    if select == 8:
        chaos.main_menu1(dominio)
    #salir a consola
    if select == 9:
        os.system("exit")