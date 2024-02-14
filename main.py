
import usuarios.acciones as acciones

print("""
      
      Acciones disponibles:
        - Registro
        - Login
      
      """)

accion = input('Que quieres hacer ? ')

manejar_acciones = acciones.ManejarAcciones()

if accion == 'registro':

    manejar_acciones.registro()

elif accion == 'login':

    manejar_acciones.login()
