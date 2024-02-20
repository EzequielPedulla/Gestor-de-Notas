import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f'\nOK{usuario[1
              ]} vamos a crear una nota...')
        titulo = input('Ingrese el titulo de la nota: ')
        descripcion = input('Ingrese el contenido: ')
        
        nota = modelo.Nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()
        
        if guardar[0] >= 1:
            print(f'\n Perfecto se guardo la nota: {nota.titulo}')
        else:
            print('No se guardo la nota')
