# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: recorremos las temperaturas una vez y guardamos en la pila los días que todavía no encuentran una temperatura más alta.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        respuesta = [0] * n
        pila = []
