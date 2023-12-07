import re

def validar_expresion(patron, expresion):
  search = re.fullmatch(patron, expresion)

  if search:
    return f'La expresion "{expresion}" cumple con la expresion regular: {patron}'
  
patron1 = r'(a|b)*(ab|b)*'
patron2 = r'[0-9A-F](a|A)'
patron3 = r'([A-Z])([a-z])*'
expresion = input('Ingrese una serie de caracteres: ')

resultado1 = validar_expresion(patron1, expresion)
resultado2 = validar_expresion(patron2, expresion)
resultado3 = validar_expresion(patron3, expresion)

if resultado1 or resultado2 or resultado3:
  print(resultado1 or resultado2 or resultado3)
else:
  print(f'La expresion {expresion} no coinicide con ningun valor')




