def inverter_string(string):
  return string[::-1]

text=input('Digite uma palavra')
texto_invertido = inverter_string(text)
print(f'{text}')
print(f'{texto_invertido}')
