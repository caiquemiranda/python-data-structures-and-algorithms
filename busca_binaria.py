

# vetor utilizado para buscar
vector = [8, 3, 5, 9, 10, 22, 45, 500, 455, 900, 4253]

vector.sort()
ponteiro = 0
tamanhovetor = len(vector)
encontrado = False

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