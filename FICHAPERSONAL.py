from HELPER import Helper
from CARGOS import Cargo
from DEPARTAMENTOS import Departamento
from EMPLEADOS import Empleado
from validacionesbuscar import Validaciones
import os



# helper = Helper()
# lista = ["1). Cargo","2). Departamento","3). Empleado","4). Salir",]
# opcion = ""
# while opcion != "4":
#   os.system("cls")
#   opcion = helper.menu(lista, "Menu Ficha Personal")
#   if opcion == "1":
#     opc1=""
#     while opc1 != "3":
#       os.system("cls")
#       opc1=helper.menu(["1) Ingreso","2) Consulta","3) Salir"],["*"*20, "MANTENIMIENTO DE CARGOS", "*"*20])
#       os.system("cls")
#       if opc1 == "1":
#         while True:
#           os.system("cls")
#           print("*"*20,"INGRESO DE CARGOS","*"*20)
#           nombreCAR = input("Ingrese un cargo (1-20 caracteres): ")
#           if len(nombreCAR)>=1 and len(nombreCAR)<=20:
#             break
#           else:
#             input("Numero de caracteres invalidos, vuelva a ingresar.")
#         cargoing = Cargo(nombreCAR)
#         nuevoCARGO  = cargoing.registro()
#         Cargo.cargos.append(nuevoCARGO)
#         input("Cargo añadido correctamente, pulse cualquier tecla para continuar: ")
#       elif opc1 == "2":
#         print("*"*20,"LISTADO DE CARGOS","*"*20)
#         print("Codigo"," "*5,"Descripcion")
#         for cargoing in Cargo.cargos:
#           cod = cargoing["codigo"]
#           des = cargoing["cargo"]
#           car = cargoing["cargo"]
#           car = Validaciones.busCargo(car)
#           print(" "*2,cod," "*8,des,)
#         input("Pulse cualquier tecla para continuar: ")

#   elif opcion == "2":
#     opc2=""
#     while opc2 != "3":
#       os.system("cls")
#       opc2=helper.menu(["1) Ingreso","2) Consulta","3) Salir"],["*"*20, "MANTENIMIENTO DE DEPARTAMENTOS", "*"*20])
#       os.system("cls")
#       if opc2 == "1":
#         print("*"*20,"INGRESO DE DEPARTAMENTOS","*"*20)
#         nombreDEP = input("Departamento: ")
#         departamentoing = Departamento(nombreDEP)
#         nuevoDEPARTAMENTO = departamentoing.registro()
#         Departamento.departamentos.append(nuevoDEPARTAMENTO)
#         input("Departamento añadido correctamente, pulse cualquier tecla para continuar: ")
#       elif opc2 == "2":
#         print("*"*20,"LISTADO DE DEPARTAMENTOS","*"*20)
#         print("Codigo"," "*5,"Descripcion")
#         for departamentoing in Departamento.departamentos:
#           cod = departamentoing["codigo"]
#           des = departamentoing["departamento"]
#           dep = departamentoing["departamento"]
#           dep = Validaciones.busDepartamento(dep)
#           print(" "*2,cod," "*8,des,)
#         input("Pulse cualquier tecla para continuar: ")

#   elif opcion == "3":
#     opc3=""
#     while opc3 != "3":
#       os.system("cls")
#       opc3=helper.menu(["1) Ingreso","2) Consulta","3) Salir"],["*"*20, "MANTENIMIENTO DE EMPLEADOS", "*"*20])
#       os.system("cls")
#       if opc3 == "1":
#         print("*"*20,"INGRESO DE EMPLEADOS","*"*20)
#         nombreEMP = input("Ingrese nombre del empleado: ")
#         cedempleado = int(input("Ingrese la cedula del empleado: "))
#         while True:
#           carempleado = int(input("Ingrese el codigo del cargo del empleado: "))
#           Ca = Validaciones.busCargo(carempleado)
#           if carempleado == Ca:
#             print("No existe ese cargo, vuelva a intentar:")
#           else:
#             break
#         while True:
#           depempleado = int(input("Ingrese el codigo del departamento del empleado: "))
#           De = Validaciones.busDepartamento(depempleado)
#           if depempleado == De:
#             print("No existe ese departamento, vuelva a intentar:")
#           else:
#             break
#         sueldempleado = float(input("Ingrese el sueldo del empleado: "))
#         empleado = Empleado(nombreEMP,cedempleado,carempleado,depempleado,sueldempleado)
#         EMP = empleado.registro()
#         Empleado.Empleados.append(EMP)
#         input("Empleado añadido correctamente, pulse cualquier tecla para continuar: ")
#       elif opc3 == "2":
#         print("*"*20,"LISTADO DE EMPLEADOS","*"*20)
#         print("Codigo"," "*5,"Nombre"," "*5,"Cedula"," "*5,"Cargo"," "*5,"Departamento"," "*5,"Sueldo")
#         for empleado in Empleado.Empleados:
#           cod = empleado["codigo"]
#           nom = empleado["nombre"]
#           cedempleado = empleado["cedula"]
#           carempleado = empleado["cargo"]
#           descargo = Validaciones.busCargo(carempleado)
#           depempleado = empleado["departamento"]
#           desdepartamento = Validaciones.busDepartamento(depempleado)
#           sueldempleado = empleado["sueldo"]
#           emp = empleado["codigo"]
#           emp = Validaciones.busEmpleado(emp)
#           print(" "*2,cod," "*8,nom," "*5,cedempleado," "*5,descargo," "*5,desdepartamento," "*5,sueldempleado)
#         input("Pulse cualquier tecla para continuar: ")
#   else:
#         print("Gracias por visitarnos")

helper = Helper()
lista = ["1). Cargo","2). Departamento","3). Empleado","4). Salir",]
opcion = ""
while opcion != "4":
  os.system("cls")
  opcion = helper.menu(lista, "Menu Ficha Personal")
  if opcion == "1":
    opc1=""
    while opc1 != "3":
      os.system("cls")
      opc1=helper.menu(["1) Ingreso","2) Consulta","3) Salir"],["*"*20, "MANTENIMIENTO DE CARGOS", "*"*20])
      os.system("cls")
      if opc1 == "1":
        while True:
          os.system("cls")
          print("*"*20,"INGRESO DE CARGOS","*"*20)
          nombreCAR = input("Ingrese un cargo (1-20 caracteres): ")
          if len(nombreCAR)>=1 and len(nombreCAR)<=20:
            break
          else:
            input("Numero de caracteres invalidos, vuelva a ingresar.")
        cargoing = Cargo(nombreCAR)
        nuevoCARGO  = cargoing.registro()
        Cargo.cargos.append(nuevoCARGO)
        input("Cargo añadido correctamente, pulse cualquier tecla para continuar: ")
      elif opc1 == "2":
        print("*"*20,"LISTADO DE CARGOS","*"*20)
        print("Codigo"," "*5,"Descripcion")
        for cargoing in Cargo.cargos:
          cod = cargoing["codigo"]
          des = cargoing["cargo"]
          car = cargoing["cargo"]
          car = Validaciones.busCargo(car)
          print(" "*2,cod," "*8,des,)
        input("Pulse cualquier tecla para continuar: ")

  elif opcion == "2":
    opc2=""
    while opc2 != "3":
      os.system("cls")
      opc2=helper.menu(["1) Ingreso","2) Consulta","3) Salir"],["*"*20, "MANTENIMIENTO DE DEPARTAMENTOS", "*"*20])
      os.system("cls")
      if opc2 == "1":
        while True:
          os.system("cls")
          print("*"*20,"INGRESO DE DEPARTAMENTOS","*"*20)
          nombreDEP = input("Ingrese un Departamento (5-20 caracteres): ")
          if len(nombreDEP)>=5 and len(nombreDEP)<=20:
            break
          else:
            print("numero de caracteres invalidos, vuelva a ingresar: ")
        departamentoing = Departamento(nombreDEP)
        nuevoDEPARTAMENTO = departamentoing.registro()
        Departamento.departamentos.append(nuevoDEPARTAMENTO)
        input("Departamento añadido correctamente, pulse cualquier tecla para continuar: ")
      elif opc2 == "2":
        print("*"*20,"LISTADO DE DEPARTAMENTOS","*"*20)
        print("Codigo"," "*5,"Descripcion")
        for departamentoing in Departamento.departamentos:
          cod = departamentoing["codigo"]
          des = departamentoing["departamento"]
          dep = departamentoing["departamento"]
          dep = Validaciones.busDepartamento(dep)
          print(" "*2,cod," "*8,des,)
        input("Pulse cualquier tecla para continuar: ")

  elif opcion == "3":
    opc3=""
    while opc3 != "3":
      os.system("cls")
      opc3=helper.menu(["1) Ingreso","2) Consulta","3) Salir"],["*"*20, "MANTENIMIENTO DE EMPLEADOS", "*"*20])
      os.system("cls")
      if opc3 == "1":
        while True:
          os.system("cls")
          print("*"*20,"INGRESO DE EMPLEADOS","*"*20)
          nombreEMP = input("Ingrese nombre del empleado: ")
          if len(nombreEMP)>=5 and len(nombreEMP)<=20:
            break
          else:
            print("numero de caracteres invalidos, vuelva a ingresar: ")
        while True:
          os.system("cls")
          print("*"*20,"INGRESO DE EMPLEADOS","*"*20)
          cedempleado = input("Ingrese la cedula del empleado: ")
          if len(cedempleado)>=5 and len(cedempleado)<=20:
            int(cedempleado)
            break
          else:
            print("numero de caracteres invalidos, vuelva a ingresar: ")
        
        while True:
          carempleado = int(input("Ingrese el codigo del cargo del empleado: "))
          Ca = Validaciones.busCargo(carempleado)
          if carempleado == Ca:
            print("No existe ese cargo, vuelva a intentar:")
          else:
            break
        while True:
          depempleado = int(input("Ingrese el codigo del departamento del empleado: "))
          De = Validaciones.busDepartamento(depempleado)
          if depempleado == De:
            print("No existe ese departamento, vuelva a intentar:")
          else:
            break
        sueldempleado = float(input("Ingrese el sueldo del empleado: "))
        empleado = Empleado(nombreEMP,cedempleado,carempleado,depempleado,sueldempleado)
        EMP = empleado.registro()
        Empleado.Empleados.append(EMP)
        input("Empleado añadido correctamente, pulse cualquier tecla para continuar: ")
      elif opc3 == "2":
        print("*"*20,"LISTADO DE EMPLEADOS","*"*20)
        print("Codigo"," "*5,"Nombre"," "*5,"Cedula"," "*5,"Cargo"," "*5,"Departamento"," "*5,"Sueldo")
        for empleado in Empleado.Empleados:
          cod = empleado["codigo"]
          nom = empleado["nombre"]
          cedempleado = empleado["cedula"]
          carempleado = empleado["cargo"]
          descargo = Validaciones.busCargo(carempleado)
          depempleado = empleado["departamento"]
          desdepartamento = Validaciones.busDepartamento(depempleado)
          sueldempleado = empleado["sueldo"]
          emp = empleado["codigo"]
          emp = Validaciones.busEmpleado(emp)
          print(" "*2,cod," "*8,nom," "*5,cedempleado," "*5,descargo," "*5,desdepartamento," "*5,sueldempleado)
        input("Pulse cualquier tecla para continuar: ")
  else:
        print("Gracias por visitarnos")

