# Algoritmos de Pathfinding: BFS, Dijkstra y A*

Este repositorio contiene implementaciones y explicaciones de los tres algoritmos más fundamentales para la búsqueda de rutas y navegación en grafos o cuadrículas.

---

## 1. BFS (Breadth-First Search)
La **Búsqueda en Anchura** es el algoritmo más sencillo para encontrar el camino más corto en grafos no ponderados (donde todos los pasos cuestan lo mismo).

* **Lógica:** Explora todos los nodos a una distancia *k* antes de pasar a los nodos a distancia *k+1*. Utiliza una estructura de datos tipo **Cola (FIFO)**.
* **Ideal para:** Encontrar el número mínimo de saltos en redes sociales o resolver laberintos donde cada movimiento vale 1.
* **Punto débil:** No sabe manejar caminos con diferentes costos (ej. terreno difícil o tráfico).



---

## 2. Algoritmo de Dijkstra
Es el estándar para encontrar la ruta más corta cuando los caminos tienen **pesos o costos diferentes**. Es una búsqueda "uniforme".

* **Lógica:** Prioriza siempre el nodo que tenga el costo acumulado más bajo desde el origen. Utiliza una **Cola de Prioridad**.
* **Funcionamiento:** Se expande en todas las direcciones de forma radial, asegurándose de que al llegar al destino, el camino tomado sea el de menor costo total.
* **Ideal para:** Sistemas de mapas donde algunas carreteras son más rápidas que otras.



---

## 3. Algoritmo A* (A-Estrella)
Es una optimización de Dijkstra y uno de los algoritmos más utilizados en la industria de los videojuegos debido a su eficiencia.

* **Lógica:** Utiliza una **heurística** (una estimación) para "adivinar" qué tan lejos está el objetivo. Su decisión se basa en la fórmula:
    $$f(n) = g(n) + h(n)$$
    * $g(n)$: Costo real desde el inicio.
    * $h(n)$: Estimación hasta el final (ej. distancia euclidiana).
* **Ventaja:** A diferencia de Dijkstra, A* no explora en todas direcciones; se dirige directamente hacia el objetivo, ahorrando mucho tiempo de procesamiento.



---

## Cuadro Comparativo

| Característica | BFS | Dijkstra | A* |
| :--- | :--- | :--- | :--- |
| **Tipo de Grafo** | No ponderado | Ponderado | Ponderado |
| **Estrategia** | Anchura pura | Costo acumulado | Costo + Heurística |
| **Garantiza óptimo** | Sí (en pesos iguales) | Sí | Sí (con heurística admisible) |
| **Eficiencia** | Baja/Media | Media | Muy Alta |


---

## Explicacion de Codigo

Para ejecutar el codigo seria de la siguiente manera
    
    python game.py



El codigo esta compuesto de esta manera 

```
import random
import os
import sys

sys.setrecursionlimit(5000)
```

- imprime lo necesario para poder usar todo esto 


Definicion estetica 



    RESET = "\033[0m"
    ROJO = "\033[31m"    # Muros
    VERDE = "\033[32m"   # Inicio
    AZUL = "\033[34m"    # Fin
    BLANCO = "\033[37m"  # Pasillos
    AMARILLO = "\033[33m" # Ruta
    CIAN = "\033[36m"    # Agua
