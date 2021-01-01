#Funciones de respaldos
import os

#Funcion de validacion de respaldos
def validacion_mail(dominio):
    comp_correo = os.path.isfile("qmail_"+dominio+".tar.gz")
    if comp_correo == True:
        print("El archivo de respaldo Qmail del dominio: ", dominio, "EXISTE")
    elif comp_correo == False:
        print("El archivo de respaldo Qmail del dominio", dominio, "NO EXISTE")

#Funcion de validacion de respaldos
def validacion_web(dominio):
    comp_web = os.path.isfile("www_"+dominio+".tar.gz")
    if comp_web == True:
        print("El archivo de respaldo WWW del dominio: ", dominio, "EXISTE")
    elif comp_web == False:
        print("El archivo de respaldo Qmail del dominio", dominio, "NO EXISTE")

#Crea el respaldo webmail en base al dominio asignado, este se crea en la carpeta raiz del programa
def crear_respaldo_qmail (dominio):
    os.system("tar -cvzf qmail_"+dominio+".tar.gz /var/www/vhost/"+dominio+"/")
    print("Respaldo de QMAIL creado con exito")

#Crea el respaldo web en base al dominio asignado, este se crea en la carpeta raiz del programa
def crear_respaldo_web (dominio):
    os.system("tar -cvzf www_"+dominio+".tar.gz /var/www/vhost/"+dominio+"/")
    print("Respaldo de WEB creado con exito")

#subir respaldo web
def sync_web (dominio):
    user = input("Captura tu usuario sygnology")
    os.system("rsync -vcazhi -e 'ssh -p 2222' --progress -stats "+dominio+"www_"+dominio+"tar.gz"+" "+user+":/volume2/Respaldos/Respaldo_Hosting/"+dominio+"/")
    print("Syncronizacion, exitosa: Respaldo Web Creado en Sygnology")


#subir respaldo correo
def sync_mail (dominio):
    user = input("Captura tu usuario sygnology")
    os.system("rsync -vcazhi -e 'ssh -p 2222' --progress -stats "+dominio+"www_"+dominio+"tar.gz"+" "+user+":/volume2/Respaldos/Respaldo_Hosting/"+dominio+"/")
    print("Syncronizacion, exitosa: Respaldo Web Creado en Sygnology")


def eliminacion_mail(dominio):
    os.system("rm -rf "+"qmail_"+dominio+".tar.gz")
    print("El respaldo de mail fue eliminado con exito")


def eliminacion_web(dominio):
    os.system("rm -rf "+"www_"+dominio+".tar.gz")
    print("El respaldo de web fue eliminado con exito")

    

