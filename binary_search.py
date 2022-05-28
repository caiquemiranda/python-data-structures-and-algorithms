# algoritmo de busca binária

# vetor utilizado para buscar
vector = [8, 3, 5, 9, 10, 22, 45, 500, 455, 900, 4253]

# ordenação do vetor
vector.sort()

# variavel ponteiro inicializada
ponteiro = 0

# variavel com tamanho do vetor
tamanhovetor = len(vector)

# condição de busca do numero
encontrado = False

# entrada de valor pelo usuário
numero = int(input("Digite un numero: "))

# iteração no vetor condição enquanto não for encontrado
# e tamanho do ponteiro for menor ou igual não para
while not(encontrado) and ponteiro <= tamanhovetor:	
	
	# metade do vetor
	metade = int(( ponteiro + tamanhovetor ) / 2)
	
	# se o numero estiver na metade(indice-metade) 
	# então encontrado
	if numero == vector[metade]:		
		encontrado = True
	
	# se o numero for menor
	elif numero < vector[metade]:		
		tamanhovetor = metade - 1
	
	# qualquer outra condição
	else:	
		ponteiro = metade + 1

# se econtrar o valor 
if(encontrado):
	print("posição do valor ", str(metade+1))
	print(vector)

# se não encontrar o valor
else:
	print("valor não econtrado")