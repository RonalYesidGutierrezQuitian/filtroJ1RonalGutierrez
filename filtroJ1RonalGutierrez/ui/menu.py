#Cada película incluirá elementos clave como código, nombre, género, duración y actores principales.
#sistema que atribuya un ID único a cada actor, junto con su nombre y el rol que desempeña en la película.
#no solo brinde una interfaz intuitiva para explorar y gestionar el catálogo cinematográfico, 
    #sino que también incorpore características avanzadas como la búsqueda por género y código, una organización eficiente de datos mediante diccionarios,


def sistemaGestor():
    print('SISTEMA GESTOR DE PELICULAS BLOCKBUSTER')
    oSistemaGestor = ["Administrador de Generos","Administrador de Actores","Administrador de formatos","Gestor de informes","Gestor peliculas","Salir"]
    pOSistemaGestor = enumerate(oSistemaGestor, 1)
    for i in pOSistemaGestor:
        print(i)
        return oSistemaGestor

def gestorGeneros():
    print('GESTOR DE GENEROS')
    oGestorGeneros = ["Crear genero","Listar generos","Ir Menu principal"]
    pOGgestorGeneros = enumerate(oGestorGeneros, 1)
    for i in pOGgestorGeneros:
        print(i)

def gestorActores():
    print('GESTOR DE ACTORES')
    oGestorActores = ["Crear Actor","Listar Actor","Ir Menu principal"]
    pOGestorActores = enumerate(oGestorActores, 1)
    for i in pOGestorActores:
        print(i)

def gestorFormatos():
    print('GESTOR DE FORMATOS')
    oGestorFormatos = ["Crear Actor","Listar Actor","Ir Menu principal"]
    pOGestorFormatos = enumerate(oGestorFormatos, 1)
    for i in pOGestorFormatos:
        print(i)

def gestorPeliculas():
    print('GESTOR DE PELICULAS')
    oGestorPeliculas = ["Agregar pelicula","Editar pelicula","Eliminar pelicula","Eliminar Actor","Buscar pelicula","Listar todas las peliculas","Menu principal"]
    pOGestorPeliculas = enumerate(oGestorPeliculas, 1)
    for i in pOGestorPeliculas:
        print(i)

def gestorInformes():
    print('GESTOR DE INFORMES')
    oGestorInformes = ["Listar las peliculas de un genero especifico","Listar las peliculas donde el protagonista sea Silverter Stallone","Buscar pelicula y mostrar la sinopsis y los actores","Ir Menu principal"]
    pOGestorInformes= enumerate(oGestorInformes, 1)
    for i in pOGestorInformes:
        print(i)
