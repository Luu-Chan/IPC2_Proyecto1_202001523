from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
from lista_datos import lista_datos
from lista_senales import lista_senales
from dato import dato
from senal import senal

class manejador_archivos:
    def __init__(self, ruta, raiz):
        self.ruta=ruta
        self.raiz=raiz

    def abrir_archivo(self):
        archivo= open(self.ruta,"r")
        archivo.close()
        tree = ET.parse(self.ruta)
        self.raiz=tree.getroot()   
        print("Archivo cargado exitosamente! \n")      

    def manipular_archivo(self):
        lista_senales_temporal=lista_senales()
        for senal_temporal in self.raiz('senal'):
        # Obtener atributos principales (nombre, niveles, amplitud)
            nombre_senal=senal_temporal.get('nombre')
            tiempo=senal_temporal.get('t')
            amplitud=senal_temporal.get('A')
            # Inicializamos nuestras listas
            lista_celdas_temporal=lista_datos()
            lista_celdas_patrones_temporal=lista_datos()
            for datos in senal_temporal.findall('dato'):
                tiempo_dato=datos.get('t')
                amplitud_dato=datos.get('A')
                seña_dato=datos.text
                if seña_dato !="NULL":
                    nuevo=dato(int(tiempo_dato),int(amplitud_dato),seña_dato)
                    lista_celdas_temporal.insertar_dato(nuevo)
                else:
                    nuevo=dato(int(tiempo_dato),int(amplitud_dato),0)
                    lista_celdas_temporal.insertar_dato(nuevo)
                # Inserción en lista de patrones celda
                if seña_dato !="NULL" and seña_dato != "0":
                    nuevo=dato(int(tiempo_dato),int(amplitud_dato),1)
                    lista_celdas_patrones_temporal.insertar_dato(nuevo)
                else:
                    nuevo=dato(int(tiempo_dato),int(amplitud_dato),0)
            lista_celdas_patrones_temporal.insertar_dato(nuevo)
            lista_senales_temporal.insertar_dato(senal(nombre_senal,tiempo,amplitud,
                                                lista_celdas_temporal,lista_celdas_patrones_temporal))
        lista_senales_temporal.recorrer_e_imprimir_lista()
        lista_senales_temporal.grafica_mi_lista_original()