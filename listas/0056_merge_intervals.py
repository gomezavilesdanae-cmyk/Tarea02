# Complejidad temporal: O(n log n) por el ordenamiento inicial.
# Complejidad espacial: O(n) para almacenar la lista de resultado.
# Justificación: ordenamos los n intervalos y eso es O(n log n)
# y recorrerlos es O(n), entonces la lista de intervalos fusionados
# puede almacenar hasta n intervalos.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Ordenamos la lista
        intervals.sort()
        intervalos_fusionados = []
        
        for intervalo_actual in intervals: # Evaluamos cada intervalo uno a uno
            # Si la lista está vacía o no se traslapan con el último guardado 
            if not intervalos_fusionados or intervalos_fusionados[-1][1] < intervalo_actual[0]:
                intervalos_fusionados.append(intervalo_actual)
            else:
                # Si se traslapan hacemos el límite final al valor más grande
                intervalos_fusionados[-1][1] = max(intervalos_fusionados[-1][1], intervalo_actual[1])
                
        return intervalos_fusionados
