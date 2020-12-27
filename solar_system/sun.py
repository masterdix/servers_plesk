import os
import order.day0
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
        from solar_system.earth import validacion_respaldo
        validacion_respaldo(dominio)
    #borrado de respaldo web
    if select == 2:
        from solar_system.earth import eliminacion_web
        eliminacion_web(dominio)
    #borrado de respaldo mail
    if select == 3:
        from solar_system.earth import eliminacion_mail
        eliminacion_mail(dominio)
    #creacion de respaldo web
    if select == 4:
        from solar_system.earth import crear_respaldo_web
        crear_respaldo_web(dominio)
    #creacion de respaldo mail
    if select == 5:
        from solar_system.earth import crear_respaldo_qmail
        crear_respaldo_qmail(dominio)
    #subir respaldo web
    if select == 6:
        from solar_system.earth import sync_web
        sync_web(dominio)
    #subir respaldo correo
    if select == 7:
        from solar_system.earth import sync_mail
        sync_mail(dominio)
    #regresa al menu principal
    if select == 8:
        from chaos import main_menu1
        main_menu1(dominio)
    #salir a consola
    if select == 9:
        os.system("exit")