# Complejidad temporal: O(n)
# Complejidad espacial: O(1) extra, sin contar el resultado
# Justificación: recorremos la lista dos veces, usamos variables
# para los productos izquierdo y derecho; y el arreglo resultado
# no cuenta como espacio extra según leetcode.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        respuesta = [1] * n

        # Calculamos los productos que están a la izquierda 
        izquierda = 1
        for i in range(n):
            respuesta[i] = izquierda
            izquierda *= nums[i]
            
        # Calculamos los productos a la derecha 
        derecha = 1
        for i in range(n - 1, -1, -1):
            respuesta[i] *= derecha
            derecha *= nums[i]
            
        return respuesta
