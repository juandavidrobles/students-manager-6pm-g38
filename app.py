import funciones

estudiantes = [
  {'nombre': 'kevin', 'apellido': 'correa', 'sexo': 'm', 'documento': 123451},
  {'nombre': 'Juan', 'apellido': 'Puentes', 'sexo': 'm', 'documento': 123452},
  {'nombre': 'Andrea', 'apellido': 'correa', 'sexo': 'f', 'documento': 123453},
  {'nombre': 'Andrea', 'apellido': 'tellez', 'sexo': 'f', 'documento': 123454},
  {'nombre': 'camilo', 'apellido': 'montenegro', 'sexo': 'm', 'documento': 123455}
]
funciones.mostrar_menu()
while True:
  eleccion = input("Elije un Numero para realizar una Accion: ")
  if eleccion == "1":
    funciones.mostrar_numero_estudiantes(estudiantes)
  elif eleccion == "2":
    print("Ingrese los datos del Estudiante: ")
    datos_est = funciones.crear_estudiante_con_datos_usuario()
    estudiantes.append(datos_est)
    print(datos_est, "datos guardados")
  elif eleccion == "3":
    nombre_a_buscar = input("Ingrese el Nombre del Estudiante a buscar: ")
    estudiantes_encontrados = funciones.buscar_estudiantes_por_nombre(nombre_a_buscar, estudiantes)
    if len(estudiantes_encontrados) == 0:
      print("No Existe Estudiante")
    else:
      for estudiante in estudiantes_encontrados:
        print(estudiante)
  elif eleccion == "4":
    documento_borrar = int(
      input("Ingrese el documento del estudiante a eliminar: "))
    estudiante_a_borrar = None
    for contador in estudiantes:
      if contador["documento"] == documento_borrar:
        estudiante_a_borrar = contador
        confirmacion = input(
          "Desea eliminar a este estudiante'si, no':  ")
        if confirmacion == "si":
          estudiantes.remove(contador)
          print("Estudiante Eliminado")
          break
    if estudiante_a_borrar == None:
      print("Estudiante No Encontrado")
  elif (eleccion == "5"):
    for contador in estudiantes:
      print(contador)
  if (eleccion == "6"):
    print('Cerrando programa...')
    break
