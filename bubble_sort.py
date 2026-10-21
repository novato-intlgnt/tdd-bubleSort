"""Traducción fiel, a Python, del bubbleSort de la Práctica 05.

El pseudocódigo original utiliza índices 1..n; Python utiliza 0..n-1.
El algoritmo modifica la misma lista recibida y realiza los bucles y las
comparaciones equivalentes a las expresadas en el enunciado.

Las etiquetas N1..N9 corresponden al grafo de flujo de control entregado.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class Traza:
    """Registro de nodos visitados y resultados de las condiciones."""

    nodos: List[str] = field(default_factory=list)
    decisiones: List[Tuple[str, str]] = field(default_factory=list)

    def visitar(self, nodo: str) -> None:
        self.nodos.append(nodo)

    def evaluar(self, nodo: str, condicion: bool) -> bool:
        self.visitar(nodo)
        self.decisiones.append((nodo, "V" if condicion else "F"))
        return condicion


def bubble_sort(vet: List[int], traza: Optional[Traza] = None) -> None:
    """Ordena *vet* de menor a mayor in situ.

    No devuelve otra lista. La traza es opcional y no altera el ordenamiento.
    """
    t = traza if traza is not None else Traza()
    t.visitar("N1")
    i = len(vet)

    while t.evaluar("N2", i >= 2):
        t.visitar("N3")
        j = 1  # Índice lógico inicial del pseudocódigo (base 1).

        while t.evaluar("N4", j <= i - 1):
            if t.evaluar("N5", vet[j - 1] > vet[j]):
                t.visitar("N6")
                aux = vet[j - 1]
                vet[j - 1] = vet[j]
                vet[j] = aux
            t.visitar("N7")
            j += 1

        t.visitar("N8")
        i -= 1

    t.visitar("N9")


if __name__ == "__main__":
    ejemplo = [2, 3, 1]
    traza = Traza()
    bubble_sort(ejemplo, traza)
    print("Resultado:", ejemplo)
    print("Camino:", " → ".join(traza.nodos))
    print("Decisiones:", traza.decisiones)
