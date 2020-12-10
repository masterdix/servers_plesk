import os
#Funciones de respaldos
def validacion_respaldo(dominio):
    comp_correo = os.path.isfile("./var/qmail/mailnames/"+"qmail_"+dominio+".tar.gz")
    if comp_correo == True:
        print("El archivo de respaldo Qmail del dominio: "+ dominio+ "EXISTE")
        elimi_dec=input("Desea eliminarlo?: Y o N ")
        if elimi_dec=="y":
            eliminacion_mail()
        else: respaldo_correo
    else: 
        print ("El archivo no existe, se procede con respaldo")
        menu()
    comp_web = os.path.isfile("./var/www/vhost"+"www_"+dominio+".tar.gz")
    if comp_web == True:
        print("El archivo de respaldo Web del dominio: "+ dominio+ "EXISTE")
        if elimi_dec=="y":
            eliminacion_web()
        else: respaldo_web(dominio,u_pagina)
    print("proceso de busqueda y validacion")