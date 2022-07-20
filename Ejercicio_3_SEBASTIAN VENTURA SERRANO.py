Datos={}
print ("Ingrese el número de personas: ")
n=int(input())
i=0
while i<n:
      print("Inserte los datos de la persona", i+1)
      nombres=input("Nombre: ")
      dni=(int(input("DNI: ")))
      edades=(int(input("Edad: ")))
      i=i+1
      Datos_Registrados={"Nombre": nombres, "DNI": dni,"Edad": edades}
      Edad_orden=edades
      Datos[Edad_orden]=Datos_Registrados


for Registro in sorted(Datos.values(), key=lambda x: x["Edad"]):
  print("Los datos registrados son:")
  print(Registro)
 
 
 
