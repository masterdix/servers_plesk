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

if menu_selection == 1:
    solar_system.sun.menu_resp(dominio)
if menu_selection == 2:
    print("en progreso")