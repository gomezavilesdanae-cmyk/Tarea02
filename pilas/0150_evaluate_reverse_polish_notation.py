# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: recorremos la lista una vez y la pila puede guardar hasta n elementos.

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        pila = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                pila.append(int(token))
