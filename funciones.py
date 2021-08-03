def mostrar_menu():
  a1 = "Mostrar número estudiantes = 1"
  a2 = "Añadir estudiante = 2"
  a3 = "Buscar estudiante = 3"
  a4 = "Eliminar estudiante = 4"
  a5 = "Mostrar todos los estudiantes = 5"
  a6 = "Salir del programa = 6"
  print(a1)
  print(a2)
  print(a3)
  print(a4)
  print(a5)
  print(a6)

def mostrar_numero_estudiantes(estudiantes):
  if len(estudiantes) > 0:
    print("El numero de estudiantes es:", len(estudiantes))
  else:
    print("No hay Estudiantes")

def crear_estudiante_con_datos_usuario():
  nombre_est = input("Ingrese el nombre: ")
  apellido_est = input("Ingrese el apellido: ")
  documento_est = int(input("Ingrese el documento: "))
  sexo_est = input("Ingrese el sexo: ")
  datos_est = {
    'nombre': nombre_est,
    'apellido': apellido_est,
    'documento': documento_est,
    'sexo': sexo_est
  }
  return datos_est

def buscar_estudiantes_por_nombre(nombre_a_buscar, estudiantes):
  estudiantes_encontrados = []
  nombre_a_buscar = str(nombre_a_buscar).capitalize()
  for estudiante in estudiantes:
    if estudiante["nombre"].capitalize() == nombre_a_buscar:
      estudiantes_encontrados.append(estudiante)

  return estudiantes_encontrados