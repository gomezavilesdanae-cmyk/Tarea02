# Complejidad Temporal: O(N)
# Complejidad Espacial: O(N)
# Justificación: Se utiliza re.findall para extraer todas las fracciones de la cadena de longitud N en O(N) tiempo. 
# Luego, se itera sobre K fracciones realizando sumas/restas y simplificando con el Máximo Común Divisor (math.gcd) 
# en tiempo O(log(min(|A|, B))), lo cual resulta en una complejidad temporal lineal global O(N). 
# La complejidad espacial es O(N) para almacenar las coincidencias extraídas.

import re
import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Expresión regular para encontrar numeradores con signo y denominadores
        pattern = r'([+-]?\d+)/(\d+)'
        matches = re.findall(pattern, expression)
        
        running_num = 0  # Numerador acumulado
        running_den = 1  # Denominador acumulado inicial
        
        for num_str, den_str in matches:
            num = int(num_str)
            den = int(den_str)
            
            # Fórmula de suma de fracciones: a/b + c/d = (a*d + c*b) / (b*d)
            running_num = running_num * den + num * running_den
            running_den = running_den * den
            
            # Simplificar la fracción usando el Máximo Común Divisor (MCD)
            common_gcd = math.gcd(abs(running_num), running_den)
            running_num //= common_gcd
            running_den //= common_gcd
            
        return f"{running_num}/{running_den}"
