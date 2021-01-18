#Funciones de mailing
import os

#elimina el trash y el spam del dominio
def spunge_dominio (dominio):
    os.system("for i in $(plesk bin mail -l | tr '\t' ' ' | cut -d' ' -f 3- | grep",dominio,"); do doveadm expunge -u '$i' mailbox INBOX.Spam all; done")
    os.system("for i in $(plesk bin mail -l | tr '\t' ' ' | cut -d' ' -f 3- | grep",dominio,"); do doveadm expunge -u '$i' mailbox INBOX.Trash all; done")

#elimina trash y spam de un usuario
def spunge_mail (dominio):
    web_user = input ("Captura el usuario (Sin dominio)")
    os.system("for i in $(plesk bin mail -l | tr '\t' ' ' | cut -d' ' -f 3- | grep",web_user,"@",dominio"); do doveadm expunge -u '$i' mailbox INBOX.Spam all; done")
    os.system("for i in $(plesk bin mail -l | tr '\t' ' ' | cut -d' ' -f 3- | grep",web_user,"@",dominio"); do doveadm expunge -u '$i' mailbox INBOX.Trash all; done")

#Lista los correos dentro de un dominio
def list_domain (dominio):
    os.system("/usr/local/psa/admin/sbin/mail_auth_view |grep",dominio)

#visualiza el password de un usuario
def password_user (dominio):
    web_user = input ("Captura el usuario (Sin dominio)")
    os.system("/usr/local/psa/admin/sbin/mail_auth_view |grep",web_user,"@",dominio)

#Limpia correo historico (dominio)
def hist_dominio (dominio):
    print("""
    
    Selecciona que periodo quieres eliminar

    1) Todos los mensajes de mas de una semana
    2) Todos los mensajes de mas de un mes
    3) Todos los mensajes de mas de un año

    """)
    periodo = input ("Captura tu opcion")

    if periodo == "1":
        os.system("doveadm expunge -u ",dominio," mailbox '*' before 1w")
    elif periodo == "2":
        os.system("doveadm expunge -u ",dominio," mailbox '*' before 4w")
    elif periodo == "3":
        os.system("doveadm expunge -u ",dominio," mailbox '*' before 48w")

#Limpia correo historico (usuario)
def hist_usuario (dominio):
    web_user = input ("Captura el usuario (Sin dominio)")
    print("""
    
    Selecciona que periodo quieres eliminar

    1) Todos los mensajes de mas de una semana
    2) Todos los mensajes de mas de un mes
    3) Todos los mensajes de mas de un año

    """)
    periodo = input ("Captura tu opcion")

    if periodo == "1":
        os.system("doveadm expunge -u ",web_user,"@",dominio," mailbox '*' before 1w")
    elif periodo == "2":
        os.system("doveadm expunge -u ",web_user,"@",dominio," mailbox '*' before 4w")
    elif periodo == "3":
        os.system("doveadm expunge -u ",web_user,"@",dominio," mailbox '*' before 48w")
