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
    2) Liempieza de correos electronicos.    
    """)

#submenu de respaldo
def submenu_resp():
    print("""
    Sistema de respaldos NOMADAT:
    ¿Que accion deseas realizar?:
    
    1) Validacion de respaldos (Valida que exista o no exista un respaldo)
    2) Eliminar un respaldo WEB(Elimina permanentemente del servidor)
    3) Eliminar un respaldo MAIL(Elimina permanentemente del servidor)
    4) Crear un respaldo WEB (Se crea un respaldo Web)
    5) Crear un respaldo de MAIL (Se crea un respaldo de Webmail)
    6) Subir respaldo WEB (Se respalda en la nube privada)
    7) Subir respaldo MAIL (Se respalda en la nube privada)
    8) Regresar al menu principal
    9) Salir del sistema
    """)