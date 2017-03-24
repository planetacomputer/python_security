x = 1
print(x + 3)

def say_hello_to(name):
	print("Hello " +  name)

say_hello_to("David")

if x < 2:
	print("Si, " + str(x) + " es menor que 2")
elif x == 2:
	print("x es igual a 2")
else:
	print("La comparacion no es cierta")

"""
edad = input("Introduce tu edad: ")
print(int(edad))

edadInt = int(edad)
if edadInt < 18:
	print("Eres menor de edad")
elif edadInt == 18:
	print("Tienes 18 anyos")
else:
	print("Eres mayor de edad")
"""
provincia = "Girona"
if(provincia == "Barcelona"):
	print("Oferta Barcelona")
elif(provincia == "Girona"):
	print("Oferta Girona")
elif(provincia == "Lleida" or provincia == "Tarragona"):
	print("Oferta Tarraco LLeida")
else:
	print("Oferta resto mundial")

estado = 110
while estado <= 10:
	print("Numero: " + str(estado))
	estado = estado + 1

mi_tupla = ('David', 21, 'Barcelona', True)

mi_lista = ['Jose', 21, 'Girona', True]

for i, valor in enumerate(mi_lista):
	if not isinstance(valor, bool) and isinstance(valor, int):
		mi_lista[i] = int(valor) + 1

print(mi_lista[0])
print(mi_lista[2])

foods = {}
foods["banana"] = 1
foods["yogures"] = 8
foods["lechuga"] = 6

print(foods)
print(foods['yogures'])

#print(foods['sdfs'])
print(foods.items())

if "banandsa" in foods:
	print("Si, aqui hay bananas")
	print(foods["banana"])
else:
	print("No hemos encontrado banandsa")

del foods["lechuga"]
print(foods.items())
print(len(foods))


logs = []
linea1 = {"response": "200", "date": "2010/02/07", "weight": 216}
logs.append(linea1)
linea2 = {"response": "200", "date": "2015/01/04", "weight": 123}
logs.append(linea2)

for linea in logs:
    print(linea["response"] + "  -  " + linea["date"])