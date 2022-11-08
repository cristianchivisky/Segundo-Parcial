from mi_arbol import(
    nodoArbol,
    insertar_nodo,
    inorden_empieza_con,
    eliminar_nodo,
    por_nivel,
    inorden_personajes,
    inorden_personajes_bajos,
    inorden_personajes_pesados,
    busqueda
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

for nombre, altura, peso in tabla:
    datos = {'altura': altura,
            'peso': peso}
    insertar_nodo(arbol_1, nombre, datos)

aux=input('ingrese 1 desea ingresar un nuevo personaje')
if aux=='1':
    nombre=input('ingrese el nombre del pesonaje que desea ingresar ')
    altura=input('ingrese la altura ')
    peso=input('ingrese el peso ')
    datos={'altura': int(altura), 'peso': int(peso)}
    print(datos)
    insertar_nodo(arbol_1, nombre, datos)

aux=input('ingrese 2 desea modificar un personaje')
if aux=='2':
    clave = input('Ingrese parte del nombre que desea modificar ')
    inorden_empieza_con(arbol_1, clave)
    clave = input('Ahora que conoce la clave ingresela ')
    pos = eliminar_nodo(arbol_1, clave)
    if pos:
        aux=input('si desea modificar el nombre ingrese 1, para modificar la altura ingrese 2 y para el peso 3: ')
        if aux=='1':
            name = input('Ingrese nuevo nombre ')
            print(name, pos[1])
            insertar_nodo(arbol_1, name, pos[1])
        elif aux=='2':
            altura=input('ingrese la nueva altura ')
            datos={'altura': int(altura), 'peso': pos[1][1]}
            insertar_nodo(pos[0], datos)
        elif aux=='3':
            peso=input('ingrese el nuevo peso ')
            datos={'altura': pos[1][0], 'peso': int(peso)}
            insertar_nodo(pos[0], datos)
    else:
        print('valor no encontrado en el arbol')

aux=input('ingrese 3 si desea dar de baja un personaje')
if aux=='3':
    nombre=input('ingrese el nombre del pesonaje que desea dar de baja ')
    eliminar_nodo(arbol_1, nombre)

inorden_personajes(arbol_1)
print(' personajes que miden menos de 0.90 metros')
inorden_personajes_bajos(arbol_1)
print(' personajes que pesan mas de 75 kilos')
inorden_personajes_pesados(arbol_1)
print(' listado por nivel ')
por_nivel(arbol_1)
aux=busqueda(arbol_1, 'Grogu')
if aux:
    print(aux['info'], aux['datos'])