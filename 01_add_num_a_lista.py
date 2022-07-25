# Faça um proĀrama que leia 5 números inteiros,
# adicione-os em uma lista e mostre-os.

lista = list() #Definindo a variável

for i in range(1, 6): #Repetirá a linha abaixo 5 vezes

   num = int(input(f'Digite o {i}º número: ')) #Lendo o novo número

   lista.append(num)

print(lista) #mostrando a lista