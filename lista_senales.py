from nodo_senal import nodo_senal
from grupo import grupo

class lista_senales:
    def __init__(self):
        self.primero=None
        self.contador_senales=0
    
    def formatear(self):
        self.primero = ""



    def insertar_dato(self,senal):
        if self.primero is None:
            self.primero=nodo_senal(senal=senal)
            self.contador_senales+=1
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_senal(senal=senal)
        self.contador_senales+=1
    
    def recorrer_e_imprimir_lista(self):
        print("Total de señales almacenadas:",self.contador_senales)
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")
        actual=self.primero
        while actual != None:
            print("Nombre:",actual.senal.nombre,"T:",actual.senal.tiempo,
                "Amplitud:",actual.senal.amplitudes)
            actual.senal.lista_datos.recorrer_e_imprimir_lista()
            actual.senal.lista_patrones_datos.recorrer_e_imprimir_lista()
            actual=actual.siguiente
            print("\n")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")
        print("\n")
    

    def grafica_mi_lista_original(self):
        actual=self.primero
        while actual != None:
            actual.senal.lista_datos.generar_grafica(actual.senal.nombre,
                                                    str(actual.senal.tiempo),
                                                    str(actual.senal.amplitudes))
            #actual.senal.lista_patrones_datos.recorrer_e_imprimir_lista()
            actual=actual.siguiente

    def calcular_los_patrones(self,nombre_senal):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre==nombre_senal:
                actual.senal.lista_patrones_nivel=actual.senal.lista_patrones_datos.devolver_patrones_por_nivel(actual.senal.lista_patrones_nivel)
                actual.senal.lista_patrones_nivel.recorrer_e_imprimir_lista()
                lista_patrones_temporal=actual.senal.lista_patrones_nivel
                grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
                print(grupos_sin_analizar)
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito =="-" and buffer!="":
                        cadena_grupo=actual.senal.lista_datos.devolver_cadena_del_grupo(buffer)
                        actual.senal.lista_grupos.insertar_dato(grupo=grupo(buffer,cadena_grupo))
                        buffer=""
                    else:
                        buffer=""
                actual.senal.lista_grupos.recorrer_e_imprimir_lista() 
                actual.senal.lista_grupos.generar_grafica(actual.senal.nombre, str(actual.senal.tiempo), str(actual.senal.amplitudes))
                return
            actual=actual.siguiente
        print ("No se encontró la senal")