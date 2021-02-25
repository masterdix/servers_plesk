#Funciones de respaldos
import os
from order.day0 import bcolors

#Funcion de validacion de respaldos
def validacion_mail(dominio):
    comp_correo = os.path.isfile("qmail_"+dominio+".tar.gz")
    if comp_correo == True:
        print(bcolors.green)
        print("El archivo de respaldo Qmail del dominio: ", dominio, "EXISTE")
        print(bcolors.endc)
    elif comp_correo == False:
        print(bcolors.red)
        print("El archivo de respaldo Qmail del dominio", dominio, "NO EXISTE")
        print(bcolors.endc)

#Funcion de validacion de respaldos
def validacion_web(dominio):
    comp_web = os.path.isfile("www_"+dominio+".tar.gz")
    if comp_web == True:
        print(bcolors.green)
        print("El archivo de respaldo WWW del dominio: ", dominio, "EXISTE")
        print(bcolors.endc)
    elif comp_web == False:
        print(bcolors.red)
        print("El archivo de respaldo Qmail del dominio", dominio, "NO EXISTE")
        print(bcolors.endc)
#Crea el respaldo webmail en base al dominio asignado, este se crea en la carpeta raiz del programa
def crear_respaldo_qmail (dominio):
    print(bcolors.bold)
    os.system("tar -cvzf qmail_"+dominio+".tar.gz /var/qmail/mailnames/"+dominio+"/")
    os.system("tar -cvzf www_"+dominio+".tar.gz /var/www/vhosts/"+dominio+"/")
    print(bcolors.green)
    print("Respaldo de QMAIL creado con exito")
    print("Respaldo de WEB creado con exito")
    print(bcolors.endc)

#Crea el respaldo web en base al dominio asignado, este se crea en la carpeta raiz del programa
#def crear_respaldo_web (dominio):
#    os.system("tar -cvzf www_"+dominio+".tar.gz /var/www/vhosts/"+dominio+"/")
#    print("Respaldo de WEB creado con exito")

#subir respaldo web
def sync_web (dominio):
    user = input("Captura tu usuario sygnology ")
    print(bcolors.bold)
    os.system("rsync -vcazhi -e 'ssh -p 2222' --progress -stats www_"+dominio+".tar.gz"+" "+user+"@nube.nomadat.com:/volume2/Respaldos/Respaldo_Hosting/"+dominio+"/")
    os.system("rsync -vcazhi -e 'ssh -p 2222' --progress -stats qmail_"+dominio+".tar.gz"+" "+user+"@nube.nomadat.com:/volume2/Respaldos/Respaldo_Hosting/"+dominio+"/")
    print(bcolors.green)
    print("Syncronizacion, exitosa: Respaldo Qmail Creado en Sygnology")
    print("Syncronizacion, exitosa: Respaldo Web Creado en Sygnology")
    print(bcolors.endc)

#subir respaldo correo
#def sync_mail (dominio):
#    user = input("Captura tu usuario sygnology")
#    os.system("rsync -vcazhi -e 'ssh -p 2222' --progress -stats qmail_"+dominio+".tar.gz"+" "+user+"@nube.nomadat.com:/volume2/Respaldos/Respaldo_Hosting/"+dominio+"/")
#    print("Syncronizacion, exitosa: Respaldo Web Creado en Sygnology")

#eliminacion local de respaldo mail
def eliminacion_mail(dominio):
    os.system("rm -rf "+"qmail_"+dominio+".tar.gz")
    os.system("rm -rf "+"www_"+dominio+".tar.gz")
    print(bcolors.green)
    print("El respaldo de mail fue eliminado con exito")
    print("El respaldo de web fue eliminado con exito")
    print(bcolors.endc)
    

#eliminacion local de respaldo web
#def eliminacion_web(dominio):
#    os.system("rm -rf "+"www_"+dominio+".tar.gz")
#    print("El respaldo de web fue eliminado con exito")
