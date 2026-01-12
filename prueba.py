import random
import os

def crear_tablero(f, c):
    # Creamos un tablero básico lleno de caminos vacíos
    return [[" " for _ in range(c)] for _ in range(f)]

def mostrar_tablero(tablero):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Imprimir números de columnas arriba
    encabezado = "   "
    for i in range(len(tablero[0])):
        encabezado += f"{i:<2}"
    print(encabezado)

    for i, fila in enumerate(tablero):
        # Imprimir número de fila a la izquierda
        fila_texto = f"{i:<3}"
        for celda in fila:
            fila_texto += celda + " "
        print(fila_texto)

def resolver_bfs(tablero, inicio, fin):
    # Algoritmo BFS para encontrar el camino más corto
    cola = [inicio]
    visitados = {inicio: None}
    
    while cola:
        actual = cola.pop(0)
        if actual == fin:
            break
        
        f, c = actual
        # Direcciones: arriba, abajo, izquierda, derecha
        for df, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nf, nc = f + df, c + dc
            if 0 <= nf < len(tablero) and 0 <= nc < len(tablero[0]):
                # Se puede pasar por espacio vacío o agua (~), pero no por muros (#) u obstáculos (X)
                if tablero[nf][nc] in [" ", "~", "E"] and (nf, nc) not in visitados:
                    visitados[(nf, nc)] = actual
                    cola.append((nf, nc))
    
    # Reconstruir el camino
    if fin not in visitados: return False
    paso = fin
    while paso:
        f, c = paso
        if tablero[f][c] not in ["S", "E"]:
            tablero[f][c] = "."
        paso = visitados[paso]
    return True

# --- FLUJO PRINCIPAL ---

# 1. Configuración inicial
f = int(input('¿Cuántas filas tendrá el mapa?: '))
c = int(input('¿Cuántas columnas tendrá el mapa?: '))
tablero = crear_tablero(f, c)

# Definir Inicio (S) y Salida (E)
tablero[0][0] = "S"
tablero[f-1][c-1] = "E"

# 2. Bucle para agregar obstáculos
while True:
    mostrar_tablero(tablero)
    print("\n[1] Añadir Muro (#) | [2] Añadir Agua (~) | [3] Resolver laberinto")
    opcion = input("Elige una opción: ")

    if opcion == "3":
        break

    tipo = "#" if opcion == "1" else "~"
    try:
        f_obj = int(input(f"Fila del objeto (0-{f-1}): "))
        c_obj = int(input(f"Columna del objeto (0-{c-1}): "))
        
        if tablero[f_obj][c_obj] in ["S", "E"]:
            print("¡No puedes bloquear la salida o el inicio!")
        else:
            tablero[f_obj][c_obj] = tipo
    except:
        print("Coordenadas no válidas.")

# 3. Resolución
print("\nResolviendo...")
exito = resolver_bfs(tablero, (0,0), (f-1, c-1))

mostrar_tablero(tablero)
if exito:
    print("\n¡Camino encontrado! Marcado con puntos (.).")
else:
    print("\nNo existe un camino posible con esos obstáculos.")