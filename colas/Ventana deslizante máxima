from collections import deque

# Complejidad temporal: O(n)
# Complejidad espacial: O(k)
# Justificación: Cada elemento de la lista nums se añade y se elimina de la deque a lo mostrador una vez, lo que garantiza un tiempo lineal O(n). El espacio auxiliar máximo está limitado por el tamaño k de la ventana en la deque.

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() # Almacenará los índices de los elementos
        resultado = []
        
        for i, num in enumerate(nums):
            # 1. Eliminar los índices que ya quedaron fuera de la ventana actual
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # 2. Eliminar de la cola los elementos menores que el número actual
            # (ya que no pueden ser el máximo si el número actual es mayor y más reciente)
            while dq and nums[dq[-1]] < num:
                dq.pop()
                
            # 3. Agregar el índice actual a la cola
            dq.append(i)
            
            # 4. Si ya hemos recorrido al menos k elementos, guardamos el máximo de la ventana
            if i >= k - 1:
                resultado.append(nums[dq[0]])
                
        return resultado
