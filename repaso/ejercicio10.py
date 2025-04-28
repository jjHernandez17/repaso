# Pide la edad y clasifica: niño,
# adolescente, adulto, anciano.

edad = int(input("ingresa tu edad"))

if edad <13:
    print("niño")
elif edad>=13 and edad<18:
    print("adolescente")
elif edad >=18 and edad<60:
    print("eres un adulto ")
else:
    print("anciano")
