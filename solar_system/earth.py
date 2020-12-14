import os
#Funciones de respaldos
def validacion_respaldo(dominio):
    os.system("cd /var/qmail/mailnames/")
    comp_correo = os.path.isfile("qmail_",dominio,".tar.gz")
    comp_web = os.path.isfile("/var/www/vhost","www_",dominio,".tar.gz")
    if comp_correo == True:
        print("El archivo de respaldo Qmail del dominio: ", dominio, "EXISTE")
    if comp_web == True:
        print("El archivo de respaldo WWW del dominio: ", dominio, "EXISTE")
        #revisar el tema de path en este modulo 