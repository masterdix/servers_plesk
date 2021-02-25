#baner principal
def nomadat_intro ():
    print(bcolors.red, """
        
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
        """, bcolors.endc)


#menu principal
def main_menu():
    print("""
    Bienvenido al sistema SSH NOMADAT:
    
    1) Respaldo (Hostings / Syncronizacion Synology)
    2) Limpieza de correos electronicos.    
    """)

#submenu de respaldo
def submenu_resp():
    print("""
    Sistema de respaldos NOMADAT:
    
    1) Validacion de respaldo de Mail (Local)
    2) Validacion de respaldo Web (Local)
    3) Eliminar un respaldo WEB (Local/Solo respaldo)
    4) Eliminar un respaldo MAIL (Local/Solo respaldo)
    5) Crear un respaldo WEB
    6) Crear un respaldo de MAIL
    7) Subir respaldo WEB (Subida syg)
    8) Subir respaldo MAIL (Subida syg)
    
    9) Regresar al menu principal
    10) Salir del sistema
    """)

def submenu_mail():
    print("""
    Sistema de correos NOMADAT:
    
    1) Listar correos de dominio (Webmail)
    2) Visualizar password correo (Webmail)
    3) Limpiar Trash/Spam (Correo especifico)
    4) Limpiar Trash/Spam (Dominio)
    5) Limpiar correo Semana/Mes/Ano (Dominio)
    6) Limpiar correo Semana/Mes/Ano (Correo especifico)
    
    7) Regresar al menu principal
    8) Salir del sistema
    """)
    
class bcolors:
    red = '\033[91m'
    green = '\033[92m'
    endc = '\033[0m'
    yellow = '\u001b[33m'
