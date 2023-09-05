from nodo_dato import nodo_dato
from Patron import Patron
import sys
import os

class lista_datos:
    def __init__(self):
        self.primero=None
        self.contador_datos=0

    def insertar_dato(self,dato):
        # Si el primer nodo es nulo
        if self.primero is None:
            self.primero=nodo_dato(dato=dato)
            self.contador_datos+=1
            return
        #Temporal para recorrer nuestra lista
        actual=self.primero
        # Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_dato(dato=dato)
        self.contador_datos+=1
    

    def insertar_dato_ordenado(self, dato):
        nuevo_dato = nodo_dato(dato=dato)
        self.contador_datos += 1
        # Si la lista está vacía solo añade el nuevo nodo
        if self.primero is None:
            self.primero = nuevo_dato
            return
        # Caso especial: la nueva dato debe ser el nuevo primer nodo, debe reemplazar al primero
        if dato.tiempo < self.primero.dato.tiempo or (
                dato.tiempo == self.primero.dato.tiempo and dato.amplitud <= self.primero.dato.amplitud):
            nuevo_dato.siguiente = self.primero
            self.primero = nuevo_dato
            return
        # Si no cumple con ninguno de los casos, recorrer hasta encontrar su posición
        actual = self.primero
        while actual.siguiente is not None and (
                dato.tiempo > actual.siguiente.dato.tiempo or (
                        dato.tiempo == actual.siguiente.dato.tiempo and dato.amplitud > actual.siguiente.dato.amplitud)):
            actual = actual.siguiente
        nuevo_dato.siguiente = actual.siguiente
        actual.siguiente = nuevo_dato

    def recorrer_e_imprimir_lista(self):
        print("============================================================")
        actual=self.primero
        while actual !=None:
            print("T:",actual.dato.tiempo,"Amplitudes",actual.dato.amplitud,
                "Dato: ",actual.dato.senal)
            actual=actual.siguiente
        print("============================================================")


    def generar_grafica(self,tiempo,amplitud,senal):
        f = open('bb.dot','w')
        # configuraciones del grafo
        text ="""
            digraph G {"niveles="""+tiempo+"""","CeldasNivel="""+amplitud+""""->" """+senal+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo #iniciaria en 1
        fila_iniciada=False
        while actual != None:
            # Si mi fila actual es diferente a la que viene
            if  sentinela_de_filas!=actual.dato.tiempo:
                #print(sentinela_de_filas,actual.dato.tiempo,"hola")
                sentinela_de_filas=actual.dato.tiempo
                fila_iniciada=False
                # Cerramos la fila
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                #Abrimos la fila
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.senal)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="yellow" gradientangle="315">"""+str(actual.dato.senal)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Gafrica.png')
        print("terminado")




# método para devolver los patrones por tiempo
    def devolver_patrones_por_nivel(self,lista_patrones_nivel):
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo #iniciaria en 1
        fila_iniciada=False
        recolector_patron=""
        while actual != None:
        # si hay cambio de fila entramos al if
            if  sentinela_de_filas!=actual.dato.tiempo:
                # fila iniciada se vuelve false, por que se acaba la fila
                fila_iniciada=False
                # ya que terminamos la fila, podemos guardar los patrones
                lista_patrones_nivel.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
                recolector_patron=""
                # actualizamos el valor de la fila (tiempo)
                sentinela_de_filas=actual.dato.tiempo
            # si fila iniciada es false, quiere decir que acaba de terminar fila y debemos empezar una nueva
            if fila_iniciada==False:
                fila_iniciada=True
                #Recolectamos el valor, ya que estamos en la fila
                recolector_patron+=str(actual.dato.senal)+"-"
            else:
                #Recolectamos el valor, ya que estamos en la fila
                recolector_patron+=str(actual.dato.senal)+"-"
            actual = actual.siguiente
        # Agregamos un nuevo patrón, sería el de toda la fila, ej: 0-1-1-1
        lista_patrones_nivel.insertar_dato(Patron(sentinela_de_filas,recolector_patron))
        # devolvermos la lista llena con los patrones
        return lista_patrones_nivel

    def devolver_cadena_del_grupo(self,grupo):
        string_resultado=""
        string_temporal=""
        buffer=""
        # viene un parametro llamado grupo, es un string con este formato "1,2"
        # recorremos caracter por caracter
        for digito in grupo:
            #si es digito
            if digito.isdigit():
            #añadimos al buffer
                buffer+=digito
            else:
                # si no es buffer, lo vaciamos
                string_temporal=""
                #recorremos la lista y recuperamos los valores para este grupo
                actual = self.primero
                while actual != None:
                    if actual.dato.tiempo==int(buffer):
                        string_temporal+= str(actual.dato.senal) + ","
                    actual = actual.siguiente
                string_resultado+=string_temporal+"\n"
                buffer=""
        #devolvemos el string resultado
        return string_resultado
