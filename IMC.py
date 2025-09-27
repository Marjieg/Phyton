#Escribir un programa que pida al usuario su peso en kg y estatura en metros,
#calcule el índice de masa corporal y lo almacece en una variable, y muestre por pantalla la frase
#tu índice de masa corporal es <imc> donde <imc> es el indice de masa corpotal calculado redondeado
#con decimales

peso=float(input('Intruzca su pero en kg'))
altura=float(input('Introduzca su altura en m'))

IMC=(peso)/(altura ** 2)
print('Tu índice de masa corporal es', round(IMC, 2))