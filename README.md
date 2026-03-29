import requests
import json
import time
from complexAndres_flashP import MemoryP
from complexAndres import herr
from datetime import datetime

class AIg:
    def __init__(self):
        try:
            self.cds = MemoryP.leer("CDS.txt").strip()
            self.api_cifrada = MemoryP.leer("API_KEY.txt").strip()
            raw_key = herr.desCifra(self.cds, self.api_cifrada)
            self.api_key = raw_key.strip()
        except:
            self.api_key = None
                
        self.modelos_reserva = [
            "gemini-2.5-flash", 
            "gemini-2.0-flash", 
            "gemini-2.5-flash-lite",
            "gemini-2.0-flash-lite",
            "gemini-1.5-flash",
            "gemini-pro"
        ]
        self.indice_modelo = 0
        self.historial = []
        self.actualizar_config()

    def actualizar_config(self):
        self.modelo_actual = self.modelos_reserva[self.indice_modelo]
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.modelo_actual}:generateContent?key={self.api_key}"

    def contexto(self, texto):
        self.historial.append({"role": "user", "parts": [{"text": str(texto)}]})

    def respuesta(self):
        if not self.api_key:
            return "[ERROR_SISTEMA]: LLAVE_API_NULA"

        intentos = 0
        max_intentos = len(self.modelos_reserva)

        while intentos < max_intentos:
            payload = {"contents": self.historial}
            headers = {'Content-Type': 'application/json'}

            try:
                res = requests.post(self.url, json=payload, headers=headers, timeout=20)
                
                if res.status_code == 200:
                    data = res.json()
                    texto_ia = data['candidates'][0]['content']['parts'][0]['text']
                    self.historial.append({"role": "model", "parts": [{"text": texto_ia}]})
                    return texto_ia

                elif res.status_code in [404, 429]:
                    estado = "NO_EXISTE" if res.status_code == 404 else "CUOTA_AGOTADA"
                    print(f"[NUCLEO]: {self.modelo_actual} -> {estado}. Cambiando a modelo de reserva...")
                    
                    self.indice_modelo += 1
                    if self.indice_modelo >= max_intentos:
                        break
                    
                    self.actualizar_config()
                    intentos += 1
                    continue

                else:
                    return f"[ERROR_SISTEMA]: CODIGO_SERVIDOR_{res.status_code}"

            except Exception as e:
                return f"[ERROR_SISTEMA]: FALLO_CONEXION_{e}"

        self.indice_modelo = 0
        self.actualizar_config()
        return "[ANDRES_OS]: SERVICIOS EN REPOSO - ESPERE DE 1 A 2 MINUTOS"

    def guardar(self, n, t):
        try:
            MemoryP.crear(n, t)
            return True
        except: return False

    def corregir_codigo(self, codigo_con_error, lista_librerias):
        prompt = f"TAREA: REPARAR_CODIGO\nENTRADA: {codigo_con_error}\nLIBRERIAS: {lista_librerias}"
        self.contexto(prompt)
        return self.respuesta()
