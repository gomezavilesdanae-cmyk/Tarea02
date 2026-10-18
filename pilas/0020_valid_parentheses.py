# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: recorremos la cadena una vez y la pila puede guardar hasta n elementos

class Solution:
    def isValid(self, s: str) -> bool:
        pila = []

        for caracter in s:
            if caracter in "([{":
                pila.append(caracter)
            elif caracter in ")]}":
                if not pila:
                    return False

                ultimo = pila.pop()

                if (caracter == ")" and ultimo != "(") or \
                   (caracter == "]" and ultimo != "[") or \
                   (caracter == "}" and ultimo != "{"):
                    return False
