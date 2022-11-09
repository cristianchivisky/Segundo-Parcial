from mi_arbol import(
    nodoArbol,
    insertar_nodo,
    eliminar_nodo,
    por_nivel,
    inorden_personajes,
    inorden_personajes_bajos,
    inorden_personajes_pesados,
    busqueda,
    altura,
    postorden_grogu
)
tabla = [
    ['Darth Vader', 1.70, 65],
    ['Luke Skywalker', 1.67, 70],
    ['Leia Organa', 1.55, 57],
    ['Obi-Wan Kenobi', 1.80, 85],
    ['Han Solo', 1.76, 74],
    ['Yoda', 0.55, 30],
    ['Mandalorian', 1.87, 90],
    ['Grogu', 0.47, 35],
    ['Chewbacca', 1.99, 120],
    ['R2-D2', 0.48, 69],
    ['Padme Amidala', 1.55, 55],
    ['Qui-Gon Jinn', 1.85, 87],
    ['Rey', 1.54, 59],
    ['Darth Maul', 1.79, 76],
    ['C-3PO', 1.86, 150],
    ['Boba Fett', 1.68, 84],
    ['Mace Windu', 1.79, 96],
    ['Ahsoka Tano', 1.56, 64],
    ['Poe Dameron', 1.78, 76],
    ['Jyn Erso', 1.54, 60]
]
arbol_1=nodoArbol()

for nombre, altura1, peso in tabla:
    datos = {'altura': altura1,
            'peso': peso}
    insertar_nodo(arbol_1, nombre, datos)

aux=input('ingrese 1 desea ingresar un nuevo personaje')
if aux=='1':
    nombre=input('ingrese el nombre del pesonaje que desea ingresar ')
    altura1=input('ingrese la altura ')
    peso=input('ingrese el peso ')
    datos={'altura': float(altura1), 'peso': int(peso)}
    insertar_nodo(arbol_1, nombre, datos)

aux=input('ingrese 2 desea modificar un personaje')
if aux=='2':
    clave = input('ingrese el nombre del personaje que desea modificar ')
    pos = eliminar_nodo(arbol_1, clave)
    if pos:
        aux=input('si desea modificar el nombre ingrese 1, para modificar la altura ingrese 2 y para el peso 3: ')
        if aux=='1':
            name = input('Ingrese nuevo nombre ')
            insertar_nodo(arbol_1, name, pos[1])
        elif aux=='2':
            altura1=input('ingrese la nueva altura ')
            datos={'altura': float(altura1), 'peso': pos[1]['peso']}
            insertar_nodo(arbol_1, pos[0], datos)
        elif aux=='3':
            peso=input('ingrese el nuevo peso ')
            datos={'altura': pos[1]['altura'], 'peso': float(peso)}
            insertar_nodo(arbol_1, pos[0], datos)
    else:
        print('valor no encontrado en el arbol')

aux=input('ingrese 3 si desea dar de baja un personaje')
if aux=='3':
    nombre=input('ingrese el nombre del pesonaje que desea dar de baja ')
    eliminar_nodo(arbol_1, nombre)

inorden_personajes(arbol_1)
print()
print(' personajes que miden menos de 0.90 metros')
inorden_personajes_bajos(arbol_1)
print()
print(' personajes que pesan mas de 75 kilos')
inorden_personajes_pesados(arbol_1)
print()
print(' listado por nivel ')
por_nivel(arbol_1)
print()
aux=busqueda(arbol_1, 'Grogu')
if aux:
    print(aux['info'], aux['datos'])

alt= altura(arbol_1)
postorden_grogu(arbol_1, alt)