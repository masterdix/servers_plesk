#Estructura principal del programa
import os
import sys
import solar_system.sun
import solar_system.earth
import solar_system.venus
import order.day0

class bcolors:
    red = '\033[91m'
    green = '\033[92m'
    endc = '\033[0m'
    yellow = '\u001b[33m'
    


#intro nomadat logo
print(bcolors.red), order.day0.nomadat_intro()
print(bcolors.endc)

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
            order.day0.submenu_mail()
            select = input("Que operacion desea realizar:  ")
            
            #Lista los correos dentro de un dominio
            if select == "1":
                solar_system.venus.list_domain(dominio)
                brain(dominio)
            
            #visualiza el password de un usuario
            elif select == "2":
                solar_system.venus.password_user(dominio)
                brain(dominio)
            
            #elimina trash y spam de un usuario
            elif select == "3":
                solar_system.venus.spunge_mail(dominio)
                brain(dominio)
            
            #elimina el trash y el spam del dominio
            elif select == "4":
                solar_system.venus.spunge_dominio(dominio)
                brain(dominio)
            
            #Limpia correo historico (dominio)
            elif select == "5":
                solar_system.venus.hist_dominio(dominio)
                brain(dominio)
            
            #Limpia correo historico (usuario)
            elif select == "6":
                solar_system.venus.hist_usuario(dominio)
                brain(dominio)
            
            #sale del bucle del submenu principal
            elif select == "7":
                brain(dominio)
    #si el dominio no existe saldra del proceso.
    else :
        print(bcolors.red)
        print("El dominio no existe en este servidor.")
        print(bcolors.endc)
        sys.exit()

#inicializa el proceso.
brain(dominio)