class Departamento:
  secuencia = 1
  departamentos = [{"codigo":1,"departamento":"Administracion"}]

  def __init__(self,descrip):
    Departamento.secuencia +=1
    self.codigo = Departamento.secuencia
    self.descripcion=descrip

  def registro(self):
    return{"codigo":self.codigo,"departamento":self.descripcion}
  
