#Calentamiento
import random

#Generacion de cadenas aleatorias
def generar_cadena(alfabeto):
  longitud_maxima = random.randint(1, len(alfabeto))
  alfabeto_str = list(map(str, alfabeto))
  return ''.join(random.choice(alfabeto_str) for i in range(longitud_maxima))
    
alfabeto = {'a','b','c','d',0 ,1 ,2 ,3 ,4}

x = generar_cadena(alfabeto)
y = generar_cadena(alfabeto)

print(f'Cadena x: {x}')
print(f'Cadena y: {y}')
print(f'Longitud |x|: {len(x)}')
print(f'Longitud |y|: {len(y)}')
print(f'Concatenacion de x e y: {x + y}')
print('Potencia x^0: ε')
print(f'Potencia x^1: {x}')
print(f'Potencia x^2: {x*x}')
print('Potencia y^0: ε')
print(f'Potencia y^4: {y*4}')

