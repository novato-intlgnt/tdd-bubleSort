# Práctica 05 - Generación de pruebas unitarias (resuelta)

Entrega basada en la guía `Pr05_Unit_Testing.pdf` del curso Ingeniería de Software II.

## Contenido

- `Informe_Practica_05.docx`: informe académico editable, con diagrama, justificación y tabla de casos.
- `Informe_Practica_05.pdf`: versión lista para visualizar o imprimir.
- `actividades/desarrollo_actividades.md`: solución de las cuatro actividades.
- `actividades/grafo_flujo_control.png` y `.svg`: grafo de flujo de control.
- `actividades/grafo_flujo_control.dot`: fuente editable del grafo (Graphviz).
- `actividades/casos_prueba.csv`: tabla de casos CP1-CP4 en formato abierto.
- `codigo/bubble_sort.py`: implementación Python equivalente al pseudocódigo, con traza por nodos.
- `codigo/test_bubble_sort.py`: ocho pruebas unitarias (`unittest`), cuatro para los caminos y cuatro complementarias.
- `resultados/ejecucion_pruebas.txt`: salida real de la suite.
- `resultados/cobertura_decisiones.json`: trazas y cobertura de ramas por nodo.
- `material_original/Pr05_Unit_Testing.pdf`: enunciado de referencia.

## Reproducir resultados

Requiere Python 3.9 o superior, sin dependencias externas para el código y los tests.

```bash
cd codigo
python -m unittest -v
```

Para modificar el diagrama se necesita Graphviz:

```bash
dot -Tpng -Gdpi=170 actividades/grafo_flujo_control.dot -o actividades/grafo_flujo_control.png
```

## Resultados

Complejidad ciclomática: **V(G) = 4**. Casos: **CP1-CP4**. Cobertura de decisiones con esos cuatro casos: **100 % (6 de 6 resultados)**. Suite ejecutada: **8 pruebas correctas**.

**Nota de equivalencia:** la guía utiliza índices 1..n; Python utiliza índices 0..n-1. Por eso, `vet[j]` y `vet[j+1]` del pseudocódigo se implementan como `vet[j-1]` y `vet[j]`. La lógica de las condiciones, la secuencia de bucles y el intercambio se conservan.
# tdd-bubleSort
