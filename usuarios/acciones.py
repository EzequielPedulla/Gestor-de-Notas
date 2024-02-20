import usuarios.usuario as modelo


class ManejarAcciones:
    def registro(self):
        print('\nRegistrando en el sistema...')

        self.nombre = input('Cual es tu nombre ?: ')
        self.apellido = input('Cual es tu apellido ?: ')
        self.email = input('Introduce tu email: ')
        self.password = input('introduce tu contraseña:  ')

        usuario = modelo.Usuario(
            self.nombre, self.apellido, self.email, self.password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f'registrando {[registro[1].nombre]} y el mail es {registro[1].email}')

    def login(self):
        print('Identificate en el sistema...')

        try:
            self.email = input('Introduce tu email: ')
            self.password = input('introduce tu contraseña:  ')

            usuario = modelo.Usuario('', '', self.email, self.password)

            login = usuario.identificar()

            if self.email == login[3]:
                print(
                    f'Bienvenido {login[1]} te has registrado  el {login[5]}')
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f'Login incorrecto intentar mas tarde')

    def proximasAcciones(self, usuario):
        print('''
              -Crear nota (crear)
              -Mostrar notas (mostrar)
              -Eliminar notas (eliminar)
              -Salir (salir)
              ''')

        accion = input('Que quieres hacer ?: ')

        if accion == 'crear':
            print('Creando...')
            self.proximasAcciones(usuario)
        elif accion == 'mostrar':
            print('Mostrando...')
        elif accion == 'eliminar':
            print('Eliminando...')
        elif accion == 'salir':
            print(f'\n Ok {usuario[1]},hasta pronto')
            exit()
        else:
            print('Opcion no valida')
