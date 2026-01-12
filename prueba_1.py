import random
import os
import sys

# Aumentar límite de recursión para mapas grandes
sys.setrecursionlimit(5000)

# ===== COLORES =====
RESET = "\033[0m"
ROJO = "\033[31m"    # Muros
VERDE = "\033[32m"   # Inicio
AZUL = "\033[34m"    # Fin
BLANCO = "\033[37m"  # Pasillos
AMARILLO = "\033[33m" # Ruta
CIAN = "\033[36m"    # Agua

# ===== CONFIGURACIÓN DINÁMICA =====
os.system('cls' if os.name == 'nt' else 'clear')
print(f"{AMARILLO}--- THE HUDDLE: GENERADOR CON SISTEMA DE AGUA ---{RESET}")
try:
    filas = int(input("Filas (impar): "))
    columnas = int(input("Columnas (impar): "))
except ValueError:
    print("Por favor, introduce números enteros.")
    sys.exit()

if filas % 2 == 0: filas += 1
if columnas % 2 == 0: columnas += 1

laberinto = [['#' for _ in range(columnas)] for _ in range(filas)]

# ===== 1. DFS GENERADOR =====
def dfs_generar(x, y):
    direcciones = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 1 <= nx < filas-1 and 1 <= ny < columnas-1:
            if laberinto[nx][ny] == '#':
                laberinto[x + dx//2][y + dy//2] = '.'
                laberinto[nx][ny] = '.'
                dfs_generar(nx, ny)
                
def dfs_generar_agua(x,y):
    direcciones = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(direcciones)

    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 1 <= nx < filas-1 and 1 <= ny < columnas-1:
            if laberinto[nx][ny] == '~':
                laberinto[x + dx//2][y + dy//2] = '.'
                laberinto[nx][ny] = '.'
                dfs_generar(nx, ny)            

# Generación inicial
laberinto[1][1] = '.'
dfs_generar(1, 1)

inicio = (1, 1)
fin = (filas - 2, columnas - 2)
laberinto[inicio[0]][inicio[1]] = 'S'
laberinto[fin[0]][fin[1]] = 'E'

# ===== 2. FUNCIÓN PARA AÑADIR AGUA =====
def generar_agua(lab, probabilidad=0.15):
    """Convierte pasillos vacíos en agua basándose en una probabilidad."""
    for r in range(1, filas - 1):
        
        for c in range(1, columnas - 1):
            if lab[r][c] == '.' and random.random() < probabilidad:
                lab[r][c] = '~' 

# ===== 3. DFS DE BÚSQUEDA (ACTUALIZADO) =====
def buscar_ruta(x, y, visitados):
    if (x, y) == fin:
        return [(x, y)]
    
    visitados.add((x, y))
    
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < filas and 0 <= ny < columnas:
            # Ahora el buscador acepta pasillos (.) y agua (~)
            if laberinto[nx][ny] in ['.', '~', 'S', 'E'] and (nx, ny) not in visitados:
                resultado = buscar_ruta(nx, ny, visitados)
                if resultado:
                    return [(x, y)] + resultado
    return None

# ===== 4. VISUALIZACIÓN EN CONSOLA =====
def imprimir(lab, ruta=None):
    if ruta is None: ruta = []
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{AMARILLO}Ruta calculada (S: Inicio, E: Fin, ≈: Agua, *: Ruta):{RESET}\n")
    for r in range(len(lab)):
        for c in range(len(lab[0])):
            pos = (r, c)
            if pos == inicio:
                print(f"{VERDE}S{RESET}", end=" ")
            elif pos == fin:
                print(f"{AZUL}E{RESET}", end=" ")
            elif pos in ruta:
                print(f"{AMARILLO}*{RESET}", end=" ")
            elif lab[r][c] == '#':
                print(f"{ROJO}█{RESET}", end=" ")
            elif lab[r][c] == '~':
                print(f"{CIAN}≈{RESET}", end=" ")
            else:
                print(f"{BLANCO}·{RESET}", end=" ")
        print()

# ===== FLUJO FINAL =====
if input("¿Añadir agua al azar? (s/n): ").lower() == 's':
    generar_agua(laberinto)

ruta_encontrada = buscar_ruta(inicio[0], inicio[1], set())
imprimir(laberinto, ruta_encontrada)

while True:
    opcion = input("\n[Enter] Obstáculo | [A] Agua | [Q] Salir: ").lower()
    if opcion == 'q': break
    elif opcion == 'a':
        generar_agua(laberinto)
    
    try:
        f = int(input("Fila: "))
        c = int(input("Columna: "))
        if 0 <= f < filas and 0 <= c < columnas and laberinto[f][c] not in ['S', 'E']:
            # Si el usuario pulsa 'a', pone agua; si no, pone un muro
            laberinto[f][c] = '~' if opcion == 'a' else '#'
            nueva_ruta = buscar_ruta(inicio[0], inicio[1], set())
            imprimir(laberinto, nueva_ruta)
        else:
            print("Posición inválida.")
    except ValueError:
        print("Coordenadas no válidas.")