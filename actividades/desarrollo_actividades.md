# Práctica 05 - Actividades desarrolladas

**Objeto:** `bubbleSort(int vet[])` de la guía proporcionada. Se trata de índices de base 1 del pseudocódigo; la ejecución en Python traduce esos índices a base 0.

## 1. Grafo de flujo de control

El grafo está en `grafo_flujo_control.png`, `grafo_flujo_control.svg` y `grafo_flujo_control.dot`.

- N1: inicio e inicialización de `i`.
- N2: `i >= 2` (decisión del bucle externo).
- N3: `j = 1`.
- N4: `j <= i - 1` (decisión del bucle interno).
- N5: `vet[j] > vet[j+1]` (decisión del intercambio).
- N6: intercambio de valores.
- N7: incremento de `j`.
- N8: decremento de `i`.
- N9: fin.

**Aristas (11):** N1→N2, N2→N3, N2→N9, N3→N4, N4→N5, N4→N8, N5→N6, N5→N7, N6→N7, N7→N4, N8→N2.

## 2. Complejidad ciclomática

El grafo tiene 9 nodos, 11 aristas y 1 componente conexa:

`V(G) = E - N + 2P = 11 - 9 + 2(1) = 4`.

Comprobación independiente: 3 nodos predicado (N2, N4, N5) + 1 = 4.

## 3. Caminos independientes (cobertura de decisiones + condiciones simples)

`V` significa verdadera y `F` falsa. Las etiquetas entre paréntesis indican el resultado de la decisión en esa visita al nodo.

### CP1: No entra al bucle externo

- **Camino observado:** `N1-N2(F)-N9`.
- **Entrada:** `[7]`.
- **Salida esperada y observada:** `[7]`.

### CP2: No realiza intercambio

- **Camino observado:** `N1-N2(V)-N3-N4(V)-N5(F)-N7-N4(F)-N8-N2(F)-N9`.
- **Entrada:** `[1, 2]`.
- **Salida esperada y observada:** `[1, 2]`.

### CP3: Realiza un intercambio

- **Camino observado:** `N1-N2(V)-N3-N4(V)-N5(V)-N6-N7-N4(F)-N8-N2(F)-N9`.
- **Entrada:** `[2, 1]`.
- **Salida esperada y observada:** `[1, 2]`.

### CP4: Repite bucles interno y externo

- **Camino observado:** `N1-N2(V)-N3-N4(V)-N5(F)-N7-N4(V)-N5(V)-N6-N7-N4(F)-N8-N2(V)-N3-N4(V)-N5(V)-N6-N7-N4(F)-N8-N2(F)-N9`.
- **Entrada:** `[2, 3, 1]`.
- **Salida esperada y observada:** `[1, 2, 3]`.

## 4. Especificación de los casos de prueba

Consulte `casos_prueba.csv` para la tabla del formato solicitado y `../resultados/cobertura_decisiones.json` para las trazas y decisiones observadas.

| ID CP | Camino en el grafo | Valores de prueba | Resultado esperado |
|---|---|---|---|
| CP1 | No entra al bucle externo | `[7]` | `[7]` |
| CP2 | No realiza intercambio | `[1, 2]` | `[1, 2]` |
| CP3 | Realiza un intercambio | `[2, 1]` | `[1, 2]` |
| CP4 | Repite bucles interno y externo | `[2, 3, 1]` | `[1, 2, 3]` |

**Justificación de independencia.** CP1 cubre la salida directa del ciclo externo; CP2 incorpora el ciclo externo e interno sin intercambio; CP3 incorpora la arista N5→N6 (intercambio); CP4 incorpora una nueva repetición N7→N4 y N8→N2. Son cuatro caminos independientes en el sentido de base de caminos y son factibles para los datos indicados.

**Cobertura de decisiones.** N2 se ejercita en V y F; N4 en V y F; N5 en V y F. El total es **6 de 6 salidas de decisión = 100 %**. Cada predicado es una sola condición simple, por lo cual la cobertura de condiciones simples también se alcanza.

**Alcance.** La cobertura no demuestra que el algoritmo esté libre de defectos. Se han añadido pruebas complementarias para lista vacía, elementos repetidos, números negativos y orden inverso.
