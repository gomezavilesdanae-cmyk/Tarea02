# Complejidad temporal: O(1) para todas las operaciones (enQueue, deQueue, Front, Rear, isEmpty, isFull)
# Complejidad espacial: O(k) para almacenar el arreglo de tamaño fijo k
# Justificación: Todas las operaciones usan índices y apuntadores con aritmética modular en tiempo constante O(1). El espacio está determinado por el tamaño fijo k de la cola.

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.head = 0
        self.tail = -1
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Calculamos la nueva posición de forma circular
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # Avanzamos el frente de forma circular
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
