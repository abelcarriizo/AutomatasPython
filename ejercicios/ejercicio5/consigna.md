# Ejercicio 5

Utilizando el lenguaje de programación Python, implementar la validación de las expresiones regulares del Ejercicio 4.

Ejemplo de validación de extensiones para imágenes en Python:

```python
import re

regex = re.compile(r"jpg|png|gif|bmp|svg")
img_ext = input("Ingrese una extensión de una imagen: ")

if regex.match(img_ext):
    print('La extensión ', img_ext, ' se corresponde con la extensión de una imagen')
else:
    print('La extensión ', img_ext, ' no se corresponde con la extensión de una imagen')
```