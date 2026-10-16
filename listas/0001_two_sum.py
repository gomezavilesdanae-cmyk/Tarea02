# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: Se recorre la lista una sola vez O(n).
# Las búsquedas e inserciones en el diccionario toman tiempo constante O(1)
# y el diccionario 'indices_por_numero' puede guardar hasta n elementos en el peor caso.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices_por_numero = {} # guardamos cada número como clave y su índice como valor
        for i, num in enumerate(nums): # Recorremos la lista para obtener el índice (i) y el número actual (num)
            diferencia = target - num # la dif. para alcanzar el target
            if diferencia in indices_por_numero: # Buscamos si esa diferencia ya fue registrada
                return [indices_por_numero[diferencia], i]
            else:
                indices_por_numero[num] = i  # Guardamos el número actual y su posición 
        return []
