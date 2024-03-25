<h1 align="center"> Teste de estágio - Target Sistemas </h1>

 ### 1) Observe o trecho de código abaixo:

```bash

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

```


Ao final do processamento, qual será o valor da variável SOMA?

`R.: 91`


### 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

R.:
```bash
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
```


### 3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, `9`

b) 2, 4, 8, 16, 32, 64, `128`

c) 0, 1, 4, 9, 16, 25, 36, `49`

d) 4, 16, 36, 64, `100`

e) 1, 1, 2, 3, 5, 8, `13`

f) 2, 10, 12, 16, 17, 18, 19, `200`



### 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

`R.: Se todas as luzes estão apagadas sabemos que nenhum interruptor esta na posição de ligado, sendo assim, posso ligar o primeiro e o segundo interruptor, voltar nas salas e ver quais luzes se acenderam, nesse processo saberei a qual lâmpada o terceiro interruptor pertence. Depois volto aos interruptores novamente e desligo o primeiro interruptor, retorno as salas e descobrirei que a lâmpada que antes estava acessa e agora se apagou pertence ao primeiro interruptor e a lâmpada que continua acessa pertence ao segundo interruptor.`

### 5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

R.:
```bash
def inverter_string(string):
  return string[::-1]

text=input('Digite uma palavra')
texto_invertido = inverter_string(text)
print(f'{text}')
print(f'{texto_invertido}')
```
