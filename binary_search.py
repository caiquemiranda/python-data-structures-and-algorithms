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

while not(encontrado) and ponteiro <= tamanhovetor:	
	metade = int((ponteiro+tamanhovetor) / 2)
	
	if numero == vector[metade]:		
		encontrado = True
	
	elif numero < vector[metade]:		
		tamanhovetor = metade - 1
	
	else:	
		ponteiro = metade + 1

if(encontrado):
	print("posição do valor ", str(metade+1))
	print(vector)

else:
	print("valor não econtrado")