#main program structure

import order.day0
import solar_system.sun
import os

order.day0.nomadat_intro()

dominio = input("Con que dominio deseas trabajar?:   ")

if solar_system.sun.validacion(dominio) == True :
    order.day0.main_menu()
else :
    os.system("exit")

menu_selection = input("Que operacion desea realizar:  ")

def control (menu_selection):
    if menu_selection == 1 :
        order.day0.submenu_resp()
    else :
        print("Seleccion incorrecta vuelva a intentar")
        order.day0.nomadat_intro()

control(menu_selection)
