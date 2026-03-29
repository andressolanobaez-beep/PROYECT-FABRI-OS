import string


class Hera:
    def __init__(self):
        pass

    def comas(self, texto):
        if not isinstance(texto, str):
            raise ValueError("Se debe pasar un texto como cadena")
        return texto.strip().split(",")

    def cifra(self, codigo, texto):
        texto = str(texto)  
        base = string.printable  
        resultado = ""
        for i, c in enumerate(texto):
            if c in base:
                idx = (base.index(c) + base.index(codigo[i % len(codigo)])) % len(base)
                resultado += base[idx]
            else:
                resultado += c 
        return resultado

    def desCifra(self, codigo, texto_cifrado):
        texto_cifrado = str(texto_cifrado)
        base = string.printable
        resultado = ""
        for i, c in enumerate(texto_cifrado):
            if c in base:
                idx = (base.index(c) - base.index(codigo[i % len(codigo)])) % len(base)
                resultado += base[idx]
            else:
                resultado += c
        return resultado
    
    
herr=Hera()
