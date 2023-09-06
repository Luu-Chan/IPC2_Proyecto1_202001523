from nodo_dato import nodo_dato
from Patron import Patron
import sys
import os

class lista_datos:
    def __init__(self):
        self.primero=None
        self.contador_datos=0

    def insertar_dato(self,dato):
        if self.primero is None:
            self.primero=nodo_dato(dato=dato)
            self.contador_datos+=1
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodo_dato(dato=dato)
        self.contador_datos+=1


    def formatear(self):
        self.primero = None

        
    def insertar_dato_ordenado(self, dato):
        nuevo_dato = nodo_dato(dato=dato)
        self.contador_datos += 1
        if self.primero is None:
            self.primero = nuevo_dato
            return
        if dato.tiempo < self.primero.dato.tiempo or (
                dato.tiempo == self.primero.dato.tiempo and dato.amplitud <= self.primero.dato.amplitud):
            nuevo_dato.siguiente = self.primero
            self.primero = nuevo_dato
            return
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


    def generar_grafica(self,nombre,tiempo,amplitudes):
        f = open('bb.dot','w')
        text ="""
            digraph G {"T="""+tiempo+"""","A="""+amplitudes+""""->" """+nombre+ """" bgcolor="#3990C4" style="filled"
            subgraph cluster1 {fillcolor="blue:orange" style="filled"
            node [shape=circle fillcolor="webgreen:cyan" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo 
        fila_iniciada=False
        while actual != None:

            if  sentinela_de_filas!=actual.dato.tiempo:

                sentinela_de_filas=actual.dato.tiempo
                fila_iniciada=False

                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True

                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="orange" gradientangle="315">"""+str(actual.dato.senal)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="orange" gradientangle="315">"""+str(actual.dato.senal)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Gafrica.png')
        print("terminado")


    def devolver_patrones_por_nivel(self,lista_patrones_nivel):
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo
        fila_iniciada=False
        recolector=""
        while actual != None:
            if  sentinela_de_filas!=actual.dato.tiempo:
                fila_iniciada=False
                lista_patrones_nivel.insertar_dato(Patron(sentinela_de_filas,recolector))
                recolector=""
                sentinela_de_filas=actual.dato.tiempo
            if fila_iniciada==False:
                fila_iniciada=True
                recolector+=str(actual.dato.senal)+"-"
            else:
                recolector+=str(actual.dato.senal)+"-"
            actual = actual.siguiente
        lista_patrones_nivel.insertar_dato(Patron(sentinela_de_filas,recolector))
        return lista_patrones_nivel

    def devolver_cadena_del_grupo(self,grupo):
        string_resultado=""
        string_temporal=""
        buffer=""
        for digito in grupo:
            if digito.isdigit():
                buffer+=digito
            else:
                string_temporal=""
                actual = self.primero
                while actual != None:
                    if actual.dato.tiempo==int(buffer):
                        string_temporal+= str(actual.dato.senal) + ","
                    actual = actual.siguiente
                string_resultado+=string_temporal+"\n"
                buffer=""
        return string_resultado
