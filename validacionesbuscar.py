from CARGOS import Cargo
from DEPARTAMENTOS import Departamento
from EMPLEADOS import Empleado


class Validaciones:
  def busCargo(cod):
    car = 0
    for pos in range(0,len(Cargo.cargos)):
      cargo = Cargo.cargos[pos]
      if cargo["codigo"] == cod:
        car = cargo["cargo"]
        break
    return car

  def busDepartamento(cod):
    dep = 0
    for pos in range(0,len(Departamento.departamentos)):
      departamento = Departamento.departamentos[pos]
      if departamento["codigo"] == cod:
        dep = departamento["departamento"]
        break
    return dep

  def busEmpleado (cod):
    emp = 0
    for pos in range(0,len(Empleado.Empleados)):
      empleado = Empleado.Empleados[pos]
      if empleado["codigo"] == cod:
        emp = empleado["nombre"]
        break
    return emp