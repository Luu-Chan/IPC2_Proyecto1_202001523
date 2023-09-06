from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
from lista_datos import lista_datos
from lista_senales import lista_senales
from lista_patrones import lista_patrones
from lista_grupos import lista_grupos
from dato import dato
from senal import senal


raiz = None
lista_senales_temporal = None
lista_grupos_temporal = None
nombre_senal = None

def cargar_archivo():
    global raiz
    ruta =askopenfilename()
    archivo= open(ruta,"r")
    archivo.close()
    tree = ET.parse(ruta)
    raiz = tree.getroot() 
    print("")
    print("========Archivo Cargado exitosamente!!========== \n")
    
    
def manipular_archivo():
    global lista_senales_temporal
    global lista_grupos_temporal
    global nombre_senal
    lista_grupos_temporal= lista_grupos()
    lista_senales_temporal=lista_senales()
    global raiz
    for senal_temporal in raiz.findall('senal'):
        nombre_senal=senal_temporal.get('nombre')
        tiempo=senal_temporal.get('t')
        amplitud=senal_temporal.get('A')
        # Inicializamos nuestras listas
        lista_datos_temporal=lista_datos()
        lista_datos_patrones_temporal=lista_datos()
        lista_patrones_temporal = lista_patrones()
        lista_grupos_temporal = lista_grupos()
        for datos in senal_temporal.findall('dato'):
            tiempo_dato=datos.get('t')
            amplitud_dato=datos.get('A')
            seña_dato=datos.text
            nuevo = dato(int(tiempo_dato), int(amplitud_dato), seña_dato)
            lista_datos_temporal.insertar_dato_ordenado(nuevo)
            if seña_dato != "0":
                nuevo=dato(int(tiempo_dato),int(amplitud_dato),1)
                lista_datos_patrones_temporal.insertar_dato(nuevo)
            else:
                nuevo=dato(int(tiempo_dato),int(amplitud_dato),0)
            lista_datos_patrones_temporal.insertar_dato(nuevo)
        lista_senales_temporal.insertar_dato(senal(nombre_senal,tiempo,amplitud,
                                                lista_datos_temporal,lista_datos_patrones_temporal, lista_patrones_temporal, lista_grupos_temporal))
    lista_senales_temporal.recorrer_e_imprimir_lista()
    #lista_senales_temporal.calcular_los_patrones("Señal Facilita")
    
def mostrar_menu():
    print("=============================================="+ "\n")
    print("BIENVENIDO SELECCIONE UNA OPCION" + "\n")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir Archivo de salida")
    print("4. Mostar Datos del estudiante")
    print("5. Generar grafica")
    print("6. Inicializar Sistema")
    print("7. Salir")
    print("")


while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    if opcion == "1":
        cargar_archivo()
        
    elif opcion == "2":
        print("")
        manipular_archivo()
        print("Los datos han sido procesados correctamente!! \n")

    elif opcion == "3": 
        print("Creando informe, espere...." + "\n")

    elif opcion == "4":
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")
        print("Datos del estudiante:")
        print("Nombre: Luis Gabriel Lopez Polanco")
        print("Carnet: 202001523")
        print("DPI: 3004390830101")
        print("Curso: Introduccion a la Programacion y Computacion 2 \n")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")

    elif opcion == "5":
        
        print("Seleccione Grafica a generar:")
        print("1 - Grafica original ")
        print("2 - Grafica matriz reducida")
        eleccion = input("Ingrese una opcion: ")
        if eleccion == "1":
            print("============== Generando Grafica..........===================")
            lista_senales.grafica_mi_lista_original(lista_senales_temporal)
        else :
            print("============== Generando Grafica..........===================")
            lista_senales_temporal.calcular_los_patrones(nombre_senal)
            
        print("Grafica generada Exitosamente! \n")

    elif opcion == "6":
        print("Reiniciar Windows")
        lista_datos.formatear()

        print("Saliendo..." + "\n")
        break
    
    else:
        print("Opción inválida. Por favor, elige una opción del menú.")

#Todo los derechos reservados 2023©