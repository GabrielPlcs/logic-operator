Valor = int(input("Escribe el valor: "))
ValorMinimo = 0
ValorMaximo = 5

dentroRango = (Valor >= ValorMinimo) and (Valor <= ValorMaximo) 

if dentroRango:
	print(f"El valor {Valor} está dentro de rango")

else:
 	print(f"El valor {Valor} está fuera de rango")
