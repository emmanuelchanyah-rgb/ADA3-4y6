class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

    def __repr__(self):
        return f"[{self.nombre}]"


class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None  

    def __repr__(self):
        return f"Postre({self.nombre})"


POSTRES = []

def buscar_postre(nombre):
    for p in POSTRES:
        if p.nombre.lower() == nombre.lower():
            return p
    return None

def insertar_ordenado(postre):
    """Mantiene la lista POSTRES ordenada alfabéticamente por nombre."""
    POSTRES.append(postre)
    POSTRES.sort(key=lambda x: x.nombre.lower())


def imprimir_lista_ingredientes(cabeza):
    actual = cabeza
    if not actual:
        print("  (sin ingredientes)")
        return
    while actual:
        print(f"  - {actual.nombre}")
        actual = actual.siguiente

def mostrar_ingredientes(nombre_postre):
    postre = buscar_postre(nombre_postre)
    if not postre:
        print(f"No existe el postre '{nombre_postre}'.")
        return
    print(f"Ingredientes de '{postre.nombre}':")
    imprimir_lista_ingredientes(postre.ingredientes)


def insertar_ingrediente(nombre_postre, nuevos_ingredientes):
    postre = buscar_postre(nombre_postre)
    if not postre:
        print(f"El postre '{nombre_postre}' no existe.")
        return

    for nombre in nuevos_ingredientes:
        nuevo = NodoIngrediente(nombre)
        if not postre.ingredientes:
            postre.ingredientes = nuevo
        else:
            actual = postre.ingredientes
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    print(f"Se agregaron {len(nuevos_ingredientes)} ingrediente(s) a '{postre.nombre}'.")


def eliminar_ingrediente(nombre_postre, ingrediente):
    postre = buscar_postre(nombre_postre)
    if not postre:
        print(f"El postre '{nombre_postre}' no existe.")
        return

    actual = postre.ingredientes
    anterior = None

    while actual:
        if actual.nombre.lower() == ingrediente.lower():
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                postre.ingredientes = actual.siguiente
            print(f"Ingrediente '{ingrediente}' eliminado de '{postre.nombre}'.")
            return
        anterior = actual
        actual = actual.siguiente

    print(f"El ingrediente '{ingrediente}' no se encontró en '{postre.nombre}'.")

def dar_de_alta(nombre_postre, lista_ingredientes):
    if buscar_postre(nombre_postre):
        print(f"El postre '{nombre_postre}' ya existe.")
        return
    nuevo_postre = Postre(nombre_postre)
    cabeza = None
    actual = None

    for nombre in lista_ingredientes:
        nodo = NodoIngrediente(nombre)
        if cabeza is None:
            cabeza = nodo
            actual = nodo
        else:
            actual.siguiente = nodo
            actual = nodo

    nuevo_postre.ingredientes = cabeza
    insertar_ordenado(nuevo_postre)
    print(f"Postre '{nombre_postre}' agregado con {len(lista_ingredientes)} ingrediente(s).")

def dar_de_baja(nombre_postre):
    for i, p in enumerate(POSTRES):
        if p.nombre.lower() == nombre_postre.lower():
            POSTRES.pop(i)
            print(f"Postre '{nombre_postre}' eliminado junto con sus ingredientes.")
            return
    print(f"No se encontró el postre '{nombre_postre}'.")

#sub programa
def eliminar_duplicados():
    vistos = {}
    nuevos = []
    for p in POSTRES:
        clave = p.nombre.lower()
        if clave not in vistos:
            vistos[clave] = p
            nuevos.append(p)
        else:
    
            actual = vistos[clave].ingredientes
            while actual and actual.siguiente:
                actual = actual.siguiente
            ing = p.ingredientes
            while ing:
                if not existe_ingrediente(vistos[clave].ingredientes, ing.nombre):
                    if actual:
                        actual.siguiente = NodoIngrediente(ing.nombre)
                        actual = actual.siguiente
                    else:
                        vistos[clave].ingredientes = NodoIngrediente(ing.nombre)
                        actual = vistos[clave].ingredientes
                ing = ing.siguiente
    POSTRES.clear()
    POSTRES.extend(nuevos)
    print("Duplicados eliminados. Si se intentara usar set() daría error: 'unhashable type: list'.")

def existe_ingrediente(cabeza, nombre):
    actual = cabeza
    while actual:
        if actual.nombre.lower() == nombre.lower():
            return True
        actual = actual.siguiente
    return False

def mostrar_postres():
    if not POSTRES:
        print("No hay postres registrados.")
        return
    print("\nLista de POSTRES:")
    for p in POSTRES:
        print(f"- {p.nombre}")

def menu():
    print("\n*** MENÚ DE GESTIÓN DE POSTRES ***")
    print("1. Mostrar ingredientes de un postre")
    print("2. Insertar ingredientes a un postre")
    print("3. Eliminar un ingrediente")
    print("4. Dar de alta un postre")
    print("5. Dar de baja un postre")
    print("6. Eliminar duplicados")
    print("7. Mostrar todos los postres")
    print("0. Salir")


def main():
    dar_de_alta("Flan", ["leche", "huevo", "azúcar", "vainilla"])
    dar_de_alta("Brownie", ["chocolate", "harina", "mantequilla", "huevo"])

    while True:
        menu()
        op = input("Opción: ").strip()
        if op == '0':
            print("Saliendo...")
            break
        elif op == '1':
            n = input("Nombre del postre: ")
            mostrar_ingredientes(n)
        elif op == '2':
            n = input("Nombre del postre: ")
            s = input("Ingredientes separados por coma: ")
            insertar_ingrediente(n, [x.strip() for x in s.split(',') if x.strip()])
        elif op == '3':
            n = input("Nombre del postre: ")
            i = input("Ingrediente a eliminar: ")
            eliminar_ingrediente(n, i)
        elif op == '4':
            n = input("Nombre nuevo del postre: ")
            s = input("Ingredientes separados por coma: ")
            dar_de_alta(n, [x.strip() for x in s.split(',') if x.strip()])
        elif op == '5':
            n = input("Nombre del postre: ")
            dar_de_baja(n)
        elif op == '6':
            eliminar_duplicados()
        elif op == '7':
            mostrar_postres()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
