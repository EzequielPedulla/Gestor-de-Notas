
class ManejarAcciones:
    def registro(self):
        print('\nRegistrando en el sistema...')

        self.nombre = input('Cual es tu nombre ?: ')
        self.apellido = input('Cual es tu apellido ?: ')
        self.email = input('Introduce tu email: ')
        self.password = input('introduce tu contraseña:  ')

    def login(self):
        print('Identificate en el sistema...')
        self.email = input('Introduce tu email: ')
        self.password = input('introduce tu contraseña:  ')
