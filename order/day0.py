#baner principal
def nomadat_intro ():
    print("""
        
███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ██████╗  █████╗ ████████╗
████╗  ██║██╔═══██╗████╗ ████║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██╔██╗ ██║██║   ██║██╔████╔██║███████║██║  ██║███████║   ██║   
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║  ██║██╔══██║   ██║   
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██████╔╝██║  ██║   ██║   
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                               
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗          
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║          
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║          
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║          
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║          
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝          
        """)


#menu principal
def main_menu():
    print("""
    Bienvenido al sistema SSH NOMADAT:
    ¿Que accion deseas realizar?:
    
    1) Respaldo (Hostings / Syncronizacion Synology)
    2) Limpieza de correos electronicos.    
    """)

#submenu de respaldo
def submenu_resp():
    print("""
    Sistema de respaldos NOMADAT:
    ¿Que accion deseas realizar?:
    
    1) Validacion de respaldos (Valida que exista o no exista un respaldo mail)
    2) Validacion de respaldos (Valida que exista o no exista un respaldo web)
    3) Eliminar un respaldo WEB(Elimina permanentemente del servidor)
    4) Eliminar un respaldo MAIL(Elimina permanentemente del servidor)
    5) Crear un respaldo WEB (Se crea un respaldo Web)
    6) Crear un respaldo de MAIL (Se crea un respaldo de Webmail)
    7) Subir respaldo WEB (Se respalda en la nube privada)
    8) Subir respaldo MAIL (Se respalda en la nube privada)
    9) Regresar al menu principal
    10) Salir del sistema
    """)