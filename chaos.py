#estructura principal del programa
import os
import order.day0

#imprime el intro
order.day0.nomadat_intro()
#captura y almacena el dominio
dominio = input("Con que dominio deseas trabajar?:   ")
#llama la funcion que valida el dominio y devuelve un true si existe
from solar_system.sun import validacion
if validacion(dominio) == True :
    order.day0.main_menu()
else :
    print("El dominio no existe en este servidor.")
    os.system("exit")


#funcion que hace correr los menus, se encapsula para poder hacer referencia a ella
def main_menu1 (dominio):
    menu_selection = input("Que operacion desea realizar:  ")
    if menu_selection == 1:
        from solar_system.sun import menu_resp
        menu_resp(dominio)
    if menu_selection == 2:
        print("en progreso")

#llama a la funcion de menus
main_menu1(dominio)

