def fibonacci_seq(n):
  fibonacci = [0, 1]
  while fibonacci[-1] < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
  return fibonacci

def verificacao_do_numero(numero, fibonacci):
  if numero in fibonacci:
    return True
  else:
    return False

numero = int(input("Digite um número: "))

sequencia_fibonacci = fibonacci_seq(numero)
if verificacao_do_numero(numero, sequencia_fibonacci):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")
