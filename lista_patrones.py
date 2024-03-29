from nodo_patron import nodo_patron

class lista_patrones:
  def __init__(self):
    self.primero = None
    self.contador_patrones=0


  def insertar_dato(self,patron):
    if self.primero is None:
      self.primero = nodo_patron(patron=patron)
      self.contador_patrones+=1
      return
    actual= self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo_patron(patron=patron)
    self.contador_patrones+=1

  def eliminar(self,nivel):
    actual = self.primero
    anterior = None
    while actual and actual.patron.nivel != nivel:
      anterior=actual
      actual = actual.siguiente
    if anterior is None:
      self.primero = actual.siguiente
      actual.siguiente = None
    elif actual:
      anterior.siguiente = actual.siguiente
      actual.siguiente = None


  def recorrer_e_imprimir_lista(self):
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")
    actual = self.primero
    while actual != None:
      print(" Senales: ",actual.patron.nivel,"Reducida: ",actual.patron.cadena_patron)
      actual = actual.siguiente
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n")
  
  def encontrar_coincidencias(self):
    print("\n")
    print("\n")
    resultado = "" 
    while self.primero:
      actual = self.primero  
      temp_string = ""  
      temp_niveles = ""  
      while actual:
        if actual.patron.cadena_patron == self.primero.patron.cadena_patron:
          temp_niveles+=(str(actual.patron.nivel))+","  
        actual=actual.siguiente
      buffer=""
      for digito in temp_niveles:
        if digito.isdigit():
          buffer+=digito
        else:
          if buffer!="":
            self.eliminar(int(buffer))
            buffer=""
          else:
            buffer=""
      resultado+=temp_niveles+"--"
    return resultado 
