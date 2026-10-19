# Complejidad temporal: O(1) amortizada
# Complejidad espacial: O(n)
# Justificación: Cada elemento entra a la pila de entrada y, como máximo, se transfiere una vez a la pila de salida, por lo que el tiempo por operación en promedio es constante. El espacio es O(n) para almacenar los elementos en las pilas.

class MyQueue:

    def __init__(self):
        # Inicializamos dos listas de Python para usarlas como pilas
        self.s_entrada = []
        self.s_salida = []

    def push(self, x: int) -> None:
        # Todo elemento nuevo se agrega a la pila de entrada
        self.s_entrada.append(x)

    def pop(self) -> int:
        # Aseguramos que la pila de salida tenga los elementos ordenados en modo cola
        self._trasladar()
        return self.s_salida.pop()

    def peek(self) -> int:
        # Consultamos el elemento al frente sin sacarlo
        self._trasladar()
        return self.s_salida[-1]

    def empty(self) -> bool:
        # La cola está vacía si ambas pilas están vacías
        return not self.s_entrada and not self.s_salida

    def _trasladar(self):
        # Si la pila de salida está vacía, pasamos todo lo de la entrada a la salida
        if not self.s_salida:
            while self.s_entrada:
                self.s_salida.append(self.s_entrada.pop())
