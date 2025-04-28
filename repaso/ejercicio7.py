# Pregunta si una persona tiene licencia
# y si lleva casco. Si no tiene licencia o
# no lleva casco, no puede conducir.

requisito = input("lleva casco? ")
requisito2 = input("lleva casco? ")

if requisito == "no" or requisito2 == "no":
    print("no puede conducir ")
else:
    print("puede conducir ")
