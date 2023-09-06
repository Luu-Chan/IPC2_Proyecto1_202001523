from nodo_grupo import nodo_grupo
import os
import sys


class lista_grupos:
  def __init__(self):
    self.primero = None
    self.contador_grupos=0

  def insertar_dato(self,grupo):
    if self.primero is None:
      self.primero = nodo_grupo(grupo=grupo)
      self.contador_grupos+=1
      return
    actual= self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo_grupo(grupo=grupo)
    self.contador_grupos+=1

  def recorrer_e_imprimir_lista(self):
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")
    actual = self.primero
    while actual != None:
      print(" Grupo: ",actual.grupo.grupo_,"Señal reducida: ",actual.grupo.cadena_grupo)
      actual = actual.siguiente
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")


  def generar_grafica(self,nombre,tiempo,amplitudes):
    h = open('bb_1.dot','w')
    text ="""
      digraph G {"T="""+tiempo+"""","A="""+amplitudes+""""->" """+nombre+ """" bgcolor="#3990C4" style="filled"
      subgraph cluster1 {fillcolor="seagreen2:purple" style="filled"
      node [shape=circle fillcolor="gold:teal" style="radial" gradientangle=180]
      a0 [ label=<
      <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
    actual = self.primero
    sentinela_de_filas=actual.grupo.grupo_ 
    fila_iniciada=False
    while actual != None:
      if  sentinela_de_filas!=actual.grupo.grupo_:
        sentinela_de_filas=actual.grupo.grupo_
        fila_iniciada=False

        text+="""</TR>\n"""  
      if fila_iniciada==False:
        fila_iniciada=True
        text+="""<TR>"""  
        text+="""<TD border="3"  bgcolor="seagreen2" gradientangle="315">"""+str(actual.grupo.grupo_)+"""</TD>\n"""
        text+="""<TD border="3"  bgcolor="seagreen2" gradientangle="315">"""+str(actual.grupo.cadena_grupo)+"""</TD>\n"""
      else:
        text+="""<TD border="3"  bgcolor="seagreen2" gradientangle="315">"""+str(actual.grupo.grupo_)+"""</TD>\n"""
        text+="""<TD border="3"  bgcolor="seagreen2" gradientangle="315">"""+str(actual.grupo.cadega_grupo)+"""</TD>\n"""
      actual = actual.siguiente
    text+=""" </TR></TABLE>>];
        }
        }\n"""
    h.write(text)
    h.close()
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    os.system('dot -Tpng bb_1.dot -o Gafrica_Reducida.png')
    print("terminado")
