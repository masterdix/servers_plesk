import os
import order.day0
#funcion de validacion de dominios
def validacion (dominio):
    print("En busca del dominio: ", dominio, "dentro del servidor")
    os.system("cd /var/www/vhost/")
    comp_dominio = os.path.isdir("/var/www/vhost/"+dominio+"/")
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
    if select == "1":
        from solar_system.earth import validacion_respaldo
        validacion_respaldo(dominio)
    #borrado de respaldo web
    elif select == "2":
        from solar_system.earth import eliminacion_web
        eliminacion_web(dominio)
    #borrado de respaldo mail
    elif select == "3":
        from solar_system.earth import eliminacion_mail
        eliminacion_mail(dominio)
    #creacion de respaldo web
    elif select == "4":
        from solar_system.earth import crear_respaldo_web
        crear_respaldo_web(dominio)
    #creacion de respaldo mail
    elif select == "5":
        from solar_system.earth import crear_respaldo_qmail
        crear_respaldo_qmail(dominio)
    #subir respaldo web
    elif select == "6":
        from solar_system.earth import sync_web
        sync_web(dominio)
    #subir respaldo correo
    elif select == "7":
        from solar_system.earth import sync_mail
        sync_mail(dominio)
    #regresa al menu principal
    elif select == "8":
        from chaos import main_menu1
        main_menu1(dominio)
    #salir a consola
    elif select == "9":
        os.system("exit")

#funcion que hace correr los menus, se encapsula para poder hacer referencia a ella
def main_menu1 (dominio):
    menu_selection = input("Que operacion desea realizar:  ")
    if menu_selection == "1":
        print("si llego")
        menu_resp(dominio)
    elif menu_selection == "2":
        print("en progreso")
        return dominio
