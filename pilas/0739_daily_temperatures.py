# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: recorremos las temperaturas una vez y guardamos en la pila los días que todavía no encuentran una temperatura más alta.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        respuesta = [0] * n
        pila = []
        for i in range(n):
            while pila and temperatures[i] > temperatures[pila[-1]]:
                anterior = pila.pop()
                respuesta[anterior] = i - anterior

            pila.append(i)

        return respiesta
