import notas.nota as modelo


class Acciones:
    def crear(self, usuario):
        print(f'\nOK {usuario[1]} vamos a crear una nota...')
        titulo = input('Ingrese el titulo de la nota: ')
        descripcion = input('Ingrese el contenido: ')

        nota = modelo.Nota(usuario[0], titulo, descripcion
                           )
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'\n Perfecto se guardo la nota: {nota.titulo}')
        else:
            print('No se guardo la nota')

    def mostrar(self, usuario):
        print(f'{usuario[1]} aca tenes tus notas')

        nota = modelo.Nota(usuario[0])

        notas = nota.listar()

        for nota in notas:
            print('\n*************')
            print(nota[2])
            print(nota[3])
            print('\n*************')

    def borrar(self, usuario):
        print(f'\n {usuario[1]} vamos a borrar notas')

        titulo = input('Introduce titulo de nota a borrar: ')

        nota = modelo.Nota(usuario[0], titulo)

        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f'se borro la nota: {nota.titulo}')
        else:
            print('No se a borrado')
