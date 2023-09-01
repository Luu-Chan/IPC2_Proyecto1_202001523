from nodo_senal import nodo_senal

class lista_senales:
    def __init__(self):
        self.primero=None
        self.contador_senales=0
    
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
        print("Total de señales almacenadas:",self.contador_senales + "\n")
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
            #actual.senal.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente

    def grafica_mi_lista_de_patrones(self):
        actual=self.primero
        while actual != None:
            actual.senal.lista_patrones_datos.generar_grafica(actual.senal.nombre,
                                                    str(actual.senal.tiempo),
                                                    str(actual.senal.amplitudes))
            #actual.senal.lista_patrones_celdas.recorrer_e_imprimir_lista()
            actual=actual.siguiente
