# Complejidad Temporal: O(N)
# Complejidad Espacial: O(1)
# Justificación: Se utiliza re.fullmatch para evaluar la cadena de longitud N. El motor de expresiones regulares recorre la cadena una sola vez en tiempo lineal O(N) utilizando un autómata finito determinista, y requiere memoria constante O(1).

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Explicación del patrón de expresión regular:
        # 1. Signo inicial opcional: [+-]?
        # 2. Parte numérica (Entero o Decimal):
        #    - Al menos un dígito, punto opcional, más dígitos opcionales: \d+\.?\d*
        #    - O bien, un punto seguido obligatoriamente de al menos un dígito: \.\d+
        # 3. Notación científica opcional (e o E):
        #    - Letra 'e' o 'E', signo opcional [+-]? y al menos un dígito \d+: (?:[eE][+-]?\d+)?
        
        pattern = r'[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?'
        
        # re.fullmatch verifica que TODA la cadena cumpla exactamente con el patrón
        return re.fullmatch(pattern, s) is not None
