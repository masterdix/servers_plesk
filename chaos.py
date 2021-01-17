#Estructura principal del programa
import os
import sys
import solar_system.sun
import solar_system.earth
import solar_system.venus
import order.day0

#intro nomadat logo
order.day0.nomadat_intro()

#pide el domiinio a comprobar
dominio = input("Con que dominio deseas trabajar?:   ")

#si el dominio existe, envia un true y da un menu de opciones, si no existe finaliza
#el proceso
def brain(dominio):
    if solar_system.sun.validacion(dominio) == True :
        order.day0.main_menu()
        menu_selection = input("Que operacion desea realizar:  ")

        if menu_selection == "1":
            order.day0.submenu_resp()
            select = input("Que operacion desea realizar:  ")
        
            #validacion de existencia de respaldo mail
            if select == "1":
                solar_system.earth.validacion_mail(dominio)
                brain(dominio)
        
            #validacion de existencia de respaldo web
            elif select == "2":
                solar_system.earth.validacion_web(dominio)
                brain(dominio)
        
            #borrado de respaldo web
            elif select == "3":
                solar_system.earth.eliminacion_web(dominio)
                brain(dominio)
        
            #borrado de respaldo mail
            elif select == "4":
                solar_system.earth.eliminacion_mail(dominio)
                brain(dominio)
        
            #creacion de respaldo web
            elif select == "5":
                solar_system.earth.crear_respaldo_web(dominio)
                brain(dominio)
        
            #creacion de respaldo mail
            elif select == "6":
                solar_system.earth.crear_respaldo_qmail(dominio)
                brain(dominio)
        
            #subir respaldo web
            elif select == "7":
                solar_system.earth.sync_web(dominio)
                brain(dominio)
        
            #subir respaldo correo
            elif select == "8":
                solar_system.earth.sync_mail(dominio)
                brain(dominio)
            
            #sale del bucle del submenu principal
            elif select == "9":
                brain(dominio)
    
        #menu de operaciones con correos    
        elif menu_selection == "2":
            order.day0.submenu_mail
            select = input("Que operacion desea realizar:  ")
            
            if select == "1":
    
    #si el dominio no existe saldra del proceso.
    else :
            print("El dominio no existe en este servidor.")
            sys.exit()

#inicializa el proceso.
brain(dominio)