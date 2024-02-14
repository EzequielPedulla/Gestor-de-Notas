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
        self.email = input('Introduce tu email: ')
        self.password = input('introduce tu contraseña:  ')
