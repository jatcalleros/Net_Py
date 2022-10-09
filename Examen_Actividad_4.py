# ######################## Implementa una Agenda ##############################
##############################################################################
# --------Poder Agregar/Modificar:-------------
# Nos pide un nombre. Si el nombre se
# encuentra en la agenda, debe mostrar el telefono
# y opcionalmente modificarlo si no es correcto.
# Si el nombre no se encuentra, debe pemitir ingresar el
# Telefono correspondiente
#
# -------Buscar-----------
# Nos pide una cadena de caracteres, y nos muestra
# Todos los contactos cuyos nombres comienzan por
# dicha cadena
#
# -------Borrar------------
# Nos pide un nombre y si existe nos preguntara
# si queremos borrarlo de la Agenda
#
# -------Listar ------------
# Nos muestra todo el listado de la agenda
print("#"*52)
print("#"*20, "AGENDA", "#"*23)
print("#"*52, "\n")

agenda = {"juan": "656-672-9865"}


def menu():
    opciones_validas = ['a', 'b', 'c', 'd', 'e', 'f']
    print("Que desea hacer?:")
    print("a) Agregar una entrada.")
    print("b) Modificar una entrada.")
    print("c) Buscar por nombre")
    print("d) Borrar una entrada")
    print("e) Mostrar toda la agenda")
    print("f) Salir")
    opcion = input().lower()
    if opcion not in opciones_validas:
        print("Opcion no Valida. Ejecute el pograma Nuevo")
        exit()
    else:
        return opcion


def agregar():
    '''Agrega Nombre y telefono a la agenda'''
    nombre = str(input("Agrege el nombre de la persona:\n")).lower()
    tel = str(input("Agrege el telefono:\n"))
    agenda[nombre] = tel
    print("El nombre {} se agrego con el telefono {}".format(nombre, tel))
    print("* ~" * 20)


def modificar():
    '''Modifica la Agenda'''
    nombre = str(
        input("Ingrese el nombre para modificar el numero:\n")).lower()
    while nombre not in agenda:
        print("El nombre que ingreso no esta en la agenda. Intente de nuevo:")
        nombre = input().lower()
    nuevo_numero = str(input("Ingres el nuevo numero"))
    agenda[nombre] = nuevo_numero
    print("El numero de {} cambio a {}".format(nombre.title(), nuevo_numero))
    print("* ~" * 20)


def buscar():
    '''Busca Telefonos por Nombre'''
    contador = 0
    cadena = str(input("Cual nombre buscas?\n")).lower()
    for keys, values in agenda.items():
        if keys.find(cadena) != -1:
            print("{}: {}".format(keys, values))
            contador = + 1
    if contador == 0:
        print("No se encontro nada.\n")
    print("* ~" * 20)


def borrar():
    '''Borra elementos de la agenda'''
    nombre = str(
        input("Ingrese el nombre que desea borrar de la agenda:\n")).lower()
    while nombre not in agenda:
        print("El nombre que ingreso no esta en la agenda. Intente de nuevo:")
        nombre = input().lower()
    agenda.pop(nombre)
    print("La informacion de {} se a borrado exitosamente\n".format(nombre))
    print("* ~" * 20)


def listar_agenda():
    '''Muestra los Elementos de la agenda'''
    if len(agenda) == 0:
        print("No hay nada que mostrar en esta agenda")
    for keys, values in agenda.items():
        print("{}: {}".format(keys, values))
    print("* ~" * 20)


opcion = menu()

while opcion != 'f':
    if opcion == 'a':
        agregar()
        opcion = menu()
    if opcion == 'b':
        modificar()
        opcion = menu()
    if opcion == 'c':
        buscar()
        opcion = menu()
    if opcion == 'd':
        borrar()
        opcion = menu()
    if opcion == 'e':
        listar_agenda()
        opcion = menu()

print("La Agenda se cerro Exitosamente")
exit()
