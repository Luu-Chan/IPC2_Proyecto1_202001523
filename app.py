from tkinter.filedialog import askopenfilename
import xml.etree.ElementTree as ET
from lista_datos import lista_datos
from lista_senales import lista_senales
from dato import dato
from senal import senal


def abrir_archivo_xml(ruta_archivo):
    try:
        # Parsea el archivo XML
        tree = ET.parse(ruta_archivo)
        root = tree.getroot()
        print("Archivo cargado exitosamente! \n")
    except ET.ParseError:
        print("Error al analizar el archivo XML.")
    except FileNotFoundError:
        print("Archivo no encontrado.")



# Recuperar el xml
ruta =askopenfilename()
archivo= open(ruta,"r")
archivo.close()
tree = ET.parse(ruta)
raiz=tree.getroot()  

# Parsear para que nuestra aplicación entienda que manipulará xml


#Lectura del xml
# Definimos mi lista que guarde todas las carceles
lista_carceles_temporal=lista_senales()
for senal_temporal in raiz.findall('senal'):
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
        nuevo=dato(int(tiempo_dato),int(amplitud_dato),seña_dato)
        lista_celdas_temporal.insertar_dato(nuevo)
        # Inserción en lista de patrones celda
        if seña_dato !="NULL" and seña_dato != "0":
            nuevo=dato(int(tiempo_dato),int(amplitud_dato),1)
            lista_celdas_patrones_temporal.insertar_dato(nuevo)
        else:
            nuevo=dato(int(tiempo_dato),int(amplitud_dato),0)
            lista_celdas_patrones_temporal.insertar_dato(nuevo)
    lista_carceles_temporal.insertar_dato(senal(nombre_senal,tiempo,amplitud,
                                                lista_celdas_temporal,lista_celdas_patrones_temporal))
lista_carceles_temporal.recorrer_e_imprimir_lista()
lista_carceles_temporal.grafica_mi_lista_original()




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
        ruta_archivo = input("Ingresa la ruta del archivo XML: ")
        abrir_archivo_xml(ruta_archivo)
        
    elif opcion == "2":
        print("")

    elif opcion == "3": 
        print("Creando informe, espere...." + "\n")

    elif opcion == "4":
        print("Mostrar archivos del estudiante")

    elif opcion == "5":
        print("Generar Grafica")

    elif opcion == "6":
        print("Reiniciar Windows")

    elif opcion == "7":
        print("Saliendo..." + "\n")
        break
    
    else:
        print("Opción inválida. Por favor, elige una opción del menú.")

#Todo los derechos reservados 2023©