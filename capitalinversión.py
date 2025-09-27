#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla
#el capital obtenido en la inversión

capital = float(input('Introduzca la cantidad que desea invertir'))
interes = float(input('Introduzca la tasa de interés anual')) / 100 # para convertir a decimal
tiempo = float(input('Introduzca el número de años'))


Capitalobtenido = (capital)*(1 + interes)**(tiempo)
print('El capital obtenido es', float(Capitalobtenido))

#C= I * i^t 

