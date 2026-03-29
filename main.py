print("IMPORTAR OBLIGATORIAMENTE ast")
import ast
print("===== LIBRERIAS QUE IMPORTASTE =====\n")
with open(__file__, "r", encoding="utf-8") as f:
    codigo = f.read()
arbol = ast.parse(codigo)
librerias = set()
for nodo in ast.walk(arbol):
    if isinstance(nodo, ast.Import):
        for nombre in nodo.names:
            librerias.add(nombre.name)
    elif isinstance(nodo, ast.ImportFrom):
        librerias.add(nodo.module)
for lib in sorted(librerias):
    print(lib)


from time import *
from complexAndres_flashP import MemoryP
from complexAndres_ascii import *
from complexAndres_MULTIMEDIA import *
from PyPDF2 import PdfReader
from complexAndres_AI import *
from moviepy.editor import VideoFileClip, AudioFileClip
import pygame
import os
import sys
import subprocess
import threading
import time
import msvcrt
from random import *
from mutagen.mp3 import MP3 as MP3META
MemoryP.crear("RUTA.txt","D:\ARCHIVOS DE Andres David Solano Baez\ROBOTICA\proyectos de python\python normal\OS")
RUTA="D:\ARCHIVOS DE Andres David Solano Baez\ROBOTICA\proyectos de python\python normal\OS"
print("se necesita API_KEY de gemini google si no tiene marque 0 y si tiene pero ya la puso marque 0")
abcd=str(input("C>="))
abcde=herr.cifra(MemoryP.leer("CDS.txt"),abcd)
MemoryP.crear("API_KEY.txt",abcde)
print("REVISANDO SISTEMA...")
exec(MemoryP.leer("API KEY.py"))
exec(MemoryP.leer("Gemini AI.py"))

print("\033[34m")
print("SU RUTA ACTUAL ES: ",os.getcwd())
MemoryP.guardar_todoUSB(RUTA)
sys.path.append(RUTA)
t = MemoryP.leer("TIEMPO.txt")
T = float(t)

print("\033[92m")
cada_cantidad_de_bytes_1_segundo=0
print("EN QUE DISPOSITIVO DE ALMACENAMIENTO UTILIZAS?: ")
print("1. DISQUETE")
print("2. SSD ANTIGUO")
print("3. SSD MODERNO")
print("4. MEMORIA MODERNA")
print("5. MEMORIA FUTURISTICA")
print("0. DISQUETE ANTIGUISIMO")
afl=str(input("[SELECT]C>="))
match afl:
    case "1":
        cada_cantidad_de_bytes_1_segundo=500
    case "2":
        cada_cantidad_de_bytes_1_segundo=10000
    case "3":
        cada_cantidad_de_bytes_1_segundo=1000000
    case "4":
        cada_cantidad_de_bytes_1_segundo=1000000000
    case "5":
        cada_cantidad_de_bytes_1_segundo=1000000000000000
    case "0":
        cada_cantidad_de_bytes_1_segundo=1

largo_barra=50
ca=cada_cantidad_de_bytes_1_segundo
largo=100
ba=largo
print(ca)
VID=VIDEO()
asci.barra(1,100)
print("\033[92m")
INI = MP3()
INI.reproducir("INICIO OS.mp3")
sleep(T)
visor2 = IMAGEN()
visor2.mostrar("INICIO OS.png")
try:
    VID.reproducir("INICIO TOTAL.mp4",True)
except Exception as ros:
        print("iniciando...")
print(asci.texto("ANDRES OS"))
sleep(T)

for d in MemoryP.solo(".app"):
    print(d); sleep(T)
for g in MemoryP.solo(".txt"):
    print(g); sleep(T)
for o in MemoryP.solo(".pdf"):
    print(o); sleep(T)
for p in MemoryP.solo(".mp3"):
    print(p); sleep(T)
for er in MemoryP.solo(".m4a"):
    print(er); sleep(T)
for img in MemoryP.solo(".png"):
    print(img); sleep(T)
for img in MemoryP.solo(".jpg"):
    print(img); sleep(T)
for img in MemoryP.solo(".jpeg"):
    print(img); sleep(T)
for vid in MemoryP.solo(".mp4"):
    print(vid); sleep(T)
for vid in MemoryP.solo(".avi"):
    print(vid); sleep(T)
for vid in MemoryP.solo(".mov"):
    print(vid); sleep(T)
for vid in MemoryP.solo(".chavo"):
    print(vid); sleep(T)

print("=====================")
sleep(T)
print("escribe 'repetir' para volver a mostrar el menu\n")

while True:
    a = input("C>=")
    if ".txt" in a:
        print("intentando leer este archivo...")
        print(MemoryP.leer(a))
        continue
    if ".pdf" in a:
        try:
            reader = PdfReader(a)
            for page in reader.pages:
                texto = page.extract_text()
                if texto:
                    print(texto)
        except Exception as e:
            print("error:", e)
        continue
    if a == "repetir":
        sleep(T)
        print(asci.texto("ANDRES OS"))
        sleep(T)
        for d in MemoryP.solo(".app"):
            print(d); sleep(T)
        for g in MemoryP.solo(".txt"):
            print(g); sleep(T)
        for o in MemoryP.solo(".pdf"):
            print(o); sleep(T)
        for p in MemoryP.solo(".mp3"):
            print(p); sleep(T)
        for er in MemoryP.solo(".m4a"):
            print(er); sleep(T)
        for img in MemoryP.solo(".png"):
            print(img); sleep(T)
        for img in MemoryP.solo(".jpg"):
            print(img); sleep(T)
        for img in MemoryP.solo(".jpeg"):
            print(img); sleep(T)
        for vid in MemoryP.solo(".mp4"):
            print(vid); sleep(T)
        for vid in MemoryP.solo(".avi"):
            print(vid); sleep(T)
        for vid in MemoryP.solo(".mov"):
            print(vid); sleep(T)
        for vid in MemoryP.solo(".chavo"):
            print(vid); sleep(T)
        print("escribe 'repetir' para volver a mostrar el menu\n")
        continue
    codigo = MemoryP.leer(a)
    if a.lower().endswith(".mp3") or a.lower().endswith(".m4a"):
        sleep(T)
        print("CARGANDO...")
        sleep(T)
        tiempo = max(1, int(MemoryP.tamaño(a) / ca))
        ti=tiempo
        asci.barra(ti,ba)
        print("¡CARGADO! DURO: ",ti)
        INI.reproducir("ABRIENDO APP.mp3")
        sleep(T)
        print(asci.texto(a))
        mp3Exten.reproducir(a)
        print("cancion terminada.....")
        continue
    if ".png" in a or ".jpg" in a or ".jpeg" in a:
        sleep(T)
        print("CARGANDO...")
        sleep(T)
        tiempo = max(1, int(MemoryP.tamaño(a) / ca))
        ti=tiempo
        asci.barra(ti,ba)
        print("¡CARGADO! DURO: ",ti)
        INI.reproducir("ABRIENDO APP.mp3")
        sleep(T)
        print(asci.texto(a))
        visor = IMAGEN()
        visor.mostrar(a,True)
        print("imagen cerrada.....")
        continue
    if ".mp4" in a or ".avi" in a or ".mov" in a:
        reproductor=VIDEO()
        sleep(T)
        tiempo = max(1, int(MemoryP.tamaño(a) / ca))
        ti=tiempo
        asci.barra(ti,ba)
        
        reproductor.reproducir(a,True)
        print("video terminado.....")
        continue
            
        print("CARGANDO...")
        sleep(T)
        tiempo = max(1, int(MemoryP.tamaño(a) / ca))
        ti=tiempo
        asci.barra(ti,ba)
        print("¡CARGADO! DURO: ",ti)
        INI.reproducir("ABRIENDO APP.mp3")
        sleep(T)
        print(asci.texto(a))
        reproductor = VIDEO()
        try:
            reproductor.reproducir(a)
        except Exception as e:
            print("video terminado.....")
        continue
    if a.endswith(".chavo"):
        reproductor=VIDEO()
        sleep(T)
        tiempo = max(1, int(MemoryP.tamaño(a) / ca+2))
        ti=tiempo
        asci.barra(ti,ba)
        try:
            reproductor.reproducir("INTRO RCN.mp4",True)
        except Exception as aghs:
            print("INTRO TELEVISA")
        try:
            reproductor.reproducir("INTRO TELEVISA.mp4",True)
        except Exception as sius:
            print("REPRODUCIENDO INTRO")
        try:
            w=randint(0,1)
            if w==0:
                reproductor.reproducir("INTRO CHAVO.mp4",True)
            else:
                reproductor.reproducir("INTRO DEL CHAVO DEL 8 V2.mp4",True)
        except Exception as ol:
            print(f"REPRODUCIENDO VIDEO...     'codigo de error: {ol}'")
        try:
            reproductor.reproducir(a,True)
            print("video terminado.....")
        except Exception as fiun:
            
            print("video terminado")
        continue
            
        print("CARGANDO...")
        sleep(T)
        tiempo = max(1, int(MemoryP.tamaño(a) / ca))
        ti=tiempo
        asci.barra(ti,ba)
        print("¡CARGADO! DURO: ",ti)
        INI.reproducir("ABRIENDO APP.mp3")
        sleep(T)
        print(asci.texto(a))
        reproductor = VIDEO()
        try:
            reproductor.reproducir(a,True)
        except Exception as e:
            print("video terminado.....")
        continue
    
    
    if a.endswith(".exe"):
        subprocess.Popen(a)
    if not codigo:
        print("archivo no encontrado\n")
        continue
    try:
        sleep(T)
        print("CARGANDO...")
        sleep(T)
        tiempo = max(1, int(MemoryP.tamaño(a) / ca))
        ti=tiempo
        asci.barra(ti,ba)
        print("¡CARGADO! DURO: ",ti)
        INI.reproducir("ABRIENDO APP.mp3")
        sleep(T)
        print(asci.texto(a))
        exec(codigo)
    except Exception as e:
        print("error:", e)
