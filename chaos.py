import os
import sys
import solar_system.sun
import solar_system.earth
import solar_system.venus
import order.day0

#--Estructura principal del programa, implica el menu y cada una de las opciones.--


#--Intro nomadat logo--
order.day0.nomadat_intro()

#--Pide el dominio a comprobar--
dominio = input("Con que dominio deseas trabajar?:   ")

#--Proceso principal--
def brain(dominio):
    #--Si el dominio existe, envia un true y presenta un menu de opciones, si no existe-- 
    #--finaliza el proceso--
    if solar_system.sun.validacion(dominio) == True :
        order.day0.main_menu()
        menu_selection = input("Que operacion desea realizar:  ")

        #--Presenta menu y pide opcion--
        if menu_selection == "1":
            order.day0.submenu_resp()
            select = input("Que operacion desea realizar:  ")
        
            #--Llama a la funcion de validacion de respaldo mail--
            if select == "1":
                solar_system.earth.validacion_mail(dominio)
                brain(dominio)
        
            #--Llama a la funcion de validacion de respaldo web--
            elif select == "2":
                solar_system.earth.validacion_web(dominio)
                brain(dominio)

            #--Llama a la funcion de borrado de respaldos--
            elif select == "3":
                solar_system.earth.eliminacion_mail(dominio)
                brain(dominio)
        
            #--Llama a la funcion de crear respaldos--
            elif select == "4":
                solar_system.earth.crear_respaldo_qmail(dominio)
                brain(dominio)
        
            #--Llama a la funcion que sube respaldos a la nube privada--
            elif select == "5":
                solar_system.earth.sync_web(dominio)
                brain(dominio)
            
            #--Sale del meni y comienza la menu principal nuevamente.--
            elif select == "6":
                brain(dominio)
    
        #--Menu de operaciones con correos--    
        elif menu_selection == "2":
            order.day0.submenu_mail()
            select = input("Que operacion desea realizar:  ")
            
            #--Llamma a la funcion que Lista los correos dentro de un dominio--
            if select == "1":
                solar_system.venus.list_domain(dominio)
                brain(dominio)
            
            #--Lllama la funcion que Visualiza el password de un usuario--
            elif select == "2":
                solar_system.venus.password_user(dominio)
                brain(dominio)
            
            #--Llama la funcion que elimina trash y spam de un usuario--
            elif select == "3":
                solar_system.venus.spunge_mail(dominio)
                brain(dominio)
            
            #--Llama la funcion que elimina el trash y el spam del dominio--
            elif select == "4":
                solar_system.venus.spunge_dominio(dominio)
                brain(dominio)
            
            #--Lllama la funcion que Limpia correo historico (dominio)--
            elif select == "5":
                solar_system.venus.hist_dominio(dominio)
                brain(dominio)
            
            #--Llama la funcion que Limpia correo historico (usuario)--
            elif select == "6":
                solar_system.venus.hist_usuario(dominio)
                brain(dominio)
            
            #--Sale del meni y comienza la menu principal nuevamente.--
            elif select == "7":
                brain(dominio)
                
    #--Si el dominio no existe saldra del proceso.--
    else :
        sys.exit()

#--Inicializa el proceso.--
brain(dominio)