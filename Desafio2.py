def fibonacci_sequence(limit):
    fibonacci = [0, 1]
    while fibonacci[-1] < limit:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def is_fibonacci_number(number, sequence):
    return number in sequence

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

fibonacci_seq = fibonacci_sequence(numero)

if is_fibonacci_number(numero, fibonacci_seq):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")