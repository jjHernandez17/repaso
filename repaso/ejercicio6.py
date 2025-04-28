# Pide la hora. Si es menor que 12 o
# mayor que 18, muestra "No es hora de
# trabajar".

hora = int(input("ingrese la hora "))

if hora <12 and hora > 18:
    print("no es hora de trabajar")
else: 
    print("es hora de trabajar")