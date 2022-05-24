


def fibonacci(numero):

	if (numero < 2):

		return numero

	else:

		return fibonacci(numero-1)+fibonacci(numero-2)

numero = int(input('Fibonacci :' ))

print(fibonacci(numero))