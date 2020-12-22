#estructura principal del programa
import order.day0
import solar_system.sun
import os

#imprime el intro
order.day0.nomadat_intro()
#captura y almacena el dominio
dominio = input("Con que dominio deseas trabajar?:   ")
#llama la funcion que valida el dominio y devuelve un true si existe
if solar_system.sun.validacion(dominio) == True :
    order.day0.main_menu()
else :
    os.system("exit")

#almacena la opcion que se eligio
menu_selection = input("Que operacion desea realizar:  ")
#funcion que hace correr los menus, se encapsula para poder hacer referencia a ella
def main_menu1 (dominio, menu_selection):
    if menu_selection == 1:
        solar_system.sun.menu_resp(dominio)
    if menu_selection == 2:
        print("en progreso")

#llama a la funcion de menus
main_menu1(dominio, menu_selection)