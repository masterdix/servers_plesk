import os
import solar_system.sun
import chaos
#Funciones de respaldos

#Funcion de validacion de respaldos
def validacion_respaldo(dominio):
    #comprueba en el directorio que exista el archivo devuelve un true o false
    comp_correo = os.path.isfile("/var/qmail/mailnames/"+"qmail_"+dominio+".tar.gz")
    comp_web = os.path.isfile("/var/www/vhost/"+"www_"+dominio+".tar.gz")
    if comp_correo == True:
        print("El archivo de respaldo Qmail del dominio: ", dominio, "EXISTE")
        os.system("PAUSE")
        solar_system.sun.menu_resp(dominio)
    else:
        print("El archivo de respaldo Qmail del dominio", dominio, "NO EXISTE")
        os.system("PAUSE")
        solar_system.sun.menu_resp(dominio)
    if comp_web == True:
        print("El archivo de respaldo WWW del dominio: ", dominio, "EXISTE")
        os.system("PAUSE")
        solar_system.sun.menu_resp(dominio)
    else: 
        print("El archivo de respaldo Qmail del dominio", dominio, "NO EXISTE")
        os.system("PAUSE")
        solar_system.sun.menu_resp(dominio)
    return dominio

#Crea el respaldo webmail en base al dominio asignado
def crear_respaldo_qmail (dominio):
    os.system("cd /var/qmail/mailnames/")
    os.system("tar -cvzf qmail_"+dominio+".tar.gz "+dominio+"/")
    print("Respaldo de QMAIL creado con exito")
    os.system("PAUSE")
    solar_system.sun.menu_resp(dominio)
    return dominio


#Crea el respaldo web en base al dominio asignado
def crear_respaldo_web (dominio):
    os.system("cd /var/www/vhost/")
    os.system("ls")
    os.system("tar -cvzf www_"+dominio+".tar.gz "+dominio+"/")
    os.system("ls")
    print("Respaldo de WEB creado con exito")
    os.system("PAUSE")
    solar_system.sun.menu_resp(dominio)
    return dominio


#subir respaldo web
def sync_web (dominio):
    os.system("cd /var/www/vhost/")
    user = input("Captura tu usuario sygnology")
    os.system("rsync -vcazhi -e 'ssh -p 2222' --progress -stats "+dominio+"www_"+dominio+"tar.gz"+" "+user+":/volume2/Respaldos/Respaldo_Hosting/"+dominio+"/")
    print("Syncronizacion, exitosa: Respaldo Web Creado en Sygnology")
    os.system("PAUSE")
    solar_system.sun.menu_resp(dominio)
    return dominio


#subir respaldo correo
def sync_mail (dominio):
    os.system("cd /var/qmail/mailnames/")
    user = input("Captura tu usuario sygnology")
    os.system("rsync -vcazhi -e 'ssh -p 2222' --progress -stats "+dominio+"www_"+dominio+"tar.gz"+" "+user+":/volume2/Respaldos/Respaldo_Hosting/"+dominio+"/")
    print("Syncronizacion, exitosa: Respaldo Web Creado en Sygnology")
    os.system("PAUSE")
    solar_system.sun.menu_resp(dominio)
    return dominio


def eliminacion_mail(dominio):
    os.system("rm -rf /var/qmail/mailnames/"+"qmail_"+dominio+".tar.gz")
    print("El respaldo de mail fue eliminado con exito")
    solar_system.sun.menu_resp(dominio)
    return dominio


def eliminacion_web(dominio):
    os.system("rm -rf /var/www/vhost/"+"www_"+dominio+".tar.gz")
    print("El respaldo de web fue eliminado con exito")
    solar_system.sun.menu_resp(dominio)
    return dominio

