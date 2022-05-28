# algortimo de permutação


# criação da função
def permutation(data, n):
    
    # se quantidade for 1 retorna o proprio valor
    if n == 1:

        # imprime o unico valor
        print(data)
        return
    
    # se tiver mais de um valor, vai iterar pela quantidade de valores 
    for i in range(n):

        permutation(data, n-1)

        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]

        else:
            data[0], data[n-1] = data[n-1], data[0]

data = [1, 2, 4, 6]
permutation(data, len(data))
