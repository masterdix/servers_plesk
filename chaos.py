#Estructura principal del programa
import os
from solar_system.sun import main_menu1
from order.day0 import nomadat_intro, main_menu


def main():
    nomadat_intro()
    dominio = input("Con que dominio deseas trabajar?:   ")
    from solar_system.sun import validacion
    if validacion(dominio) == True :
        main_menu()
        main_menu1(dominio)
    else :
        print("El dominio no existe en este servidor.")
        os.system("exit")

main()