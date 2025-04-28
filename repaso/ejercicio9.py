# Pide una nota (0-10). Muestra si
# perdio, aprobado o sobresaliente.

nota = int("digita la nota ")

if nota<=5:
    print("perdiste")
elif nota>5 and nota<8:
    print("aprobado")
elif nota>=8:
    print("sobresaliente")