#4) Faça um Programa que leia 20 números inteiros e armazene-os numa lista. Armazene os números
#pares na listar PAR e os números IMPARES na lista impar. Imprima os três vetores.

listaPar = []
listaImpar = []
listaNumeros = []
numero = 0
print('Informe os numeros:')
for i in range(20):
	listaNumeros.append((int(input('Numero: ' + str(i+1) + ':\n'))))
	numero = listaNumeros[i]
	if(numero%2 == 0):
		listaPar.append(numero)
	else:
		listaImpar.append(numero)

print("lista Numeros; ",listaNumeros)
print("lista Par; ",listaPar)
print("lista Impar; ",listaImpar)