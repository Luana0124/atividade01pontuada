import os 
os.system("clss||clear")

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = 0
menor_numero = 0
soma_pares = 0
soma_impares = 0
soma_geral = 0
lista_numero = []
lista_pares = []
lista_impares= []
# Processando cada número
for i in range(5):
   numero = int(input(" digite um numero:")) 
   lista_numero.append(numero)
   if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
        lista_pares.append(numero)
   else:
    quantidade_impares += 1
    soma_impares += numero
    lista_impares.append(numero)
    if numero>0:
     quantidade_negativos+=1
    else: 
     quantidade_positivos += 1

maior_numero = max(lista_numero)
menor_numero = min(lista_numero)

soma_geral = sum(lista_numero)
soma_pares=sum(lista_pares)
soma_impares=sum(lista_impares)
# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares > 0 else 0
media_geral = soma_geral / 5

# Imprimindo as estatísticas
print("\nEstatísticas dos números:")
print(f"Quantidade de pares: {quantidade_pares}")
print(f"Quantidade de ímpares: {quantidade_impares}")
print(f"Quantidade de positivos: {quantidade_positivos}")
print(f"Quantidade de negativos: {quantidade_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_geral:.2f}")
print(f"Números na ordem inversa:")
for numero in reversed(lista_numero):
    print( numero)