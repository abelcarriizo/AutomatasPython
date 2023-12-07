Pequeño resumen de Expresiones Regulares

## 1. Introducción a Expresiones Regulares (Regex)

### 1.1 Definición y Propósito de Regex

Las expresiones regulares, o regex, son patrones de búsqueda utilizados para encontrar cadenas de texto que coincidan con un patrón específico. Son extremadamente útiles cuando necesitas realizar operaciones de búsqueda, extracción o manipulación de texto de manera más avanzada.

**Propósitos principales:**
- Búsqueda de patrones en texto.
- Validación de formatos de cadenas.
- Extracción de información específica.

### 1.2 Aplicaciones Prácticas en Python

En Python, el módulo `re` proporciona soporte para expresiones regulares. Algunas aplicaciones prácticas incluyen:

- Validación de direcciones de correo electrónico.
- Búsqueda y extracción de números de teléfono.
- Filtrado de datos basado en patrones específicos.
- Sustitución de texto basada en patrones.

## 2. Sintaxis Básica de Regex

### 2.1 Caracteres Literales

En regex, los caracteres literales coinciden exactamente con ellos mismos. Por ejemplo, el patrón "abc" coincidirá con la cadena "abc".

### 2.2 Metacaracteres

Los metacaracteres son caracteres especiales con significados especiales en regex. Algunos de los metacaracteres básicos incluyen:

- `.`: Coincide con cualquier carácter excepto nueva línea.
- `^`: Coincide con el inicio de la cadena.
- `$`: Coincide con el final de la cadena.
- `*`: Coincide con 0 o más repeticiones del elemento anterior.
- `+`: Coincide con 1 o más repeticiones del elemento anterior.
- `?`: Coincide con 0 o 1 repetición del elemento anterior.
- `{}`: Especifica un rango de repeticiones.

**Ejemplos:**
- `a.` coincidirá con "ab", "ac", etc.
- `^abc` coincidirá con "abc" al principio de la cadena.
- `xyz$` coincidirá con "xyz" al final de la cadena.
- `ab*` coincidirá con "a", "ab", "abb", etc.

## 3. Cuantificadores y Caracteres Especiales

### 3.1 Repetición con *, +, ?

- `*`: Coincide con 0 o más repeticiones del elemento anterior.
    - Ejemplo: `ab*c` coincidirá con "ac", "abc", "abbc", etc.

- `+`: Coincide con 1 o más repeticiones del elemento anterior.
    - Ejemplo: `ab+c` coincidirá con "abc", "abbc", etc., pero no con "ac".

- `?`: Coincide con 0 o 1 repetición del elemento anterior.
    - Ejemplo: `ab?c` coincidirá con "ac" y "abc".

### 3.2 Rangos con {}

- `{n}`: Coincide exactamente con n repeticiones del elemento anterior.
    - Ejemplo: `a{3}` coincidirá con "aaa".

- `{n,}`: Coincide con n o más repeticiones del elemento anterior.
    - Ejemplo: `a{2,}` coincidirá con "aa", "aaa", etc.

- `{n,m}`: Coincide con entre n y m repeticiones del elemento anterior.
    - Ejemplo: `a{2,4}` coincidirá con "aa", "aaa" y "aaaa".

### 3.3 Uso de ^ y $ para el Inicio y Final de la Cadena

- `^`: Coincide con el inicio de la cadena.
    - Ejemplo: `^abc` coincidirá con "abc" solo si está al principio de la cadena.

- `$`: Coincide con el final de la cadena.
    - Ejemplo: `xyz$` coincidirá con "xyz" solo si está al final de la cadena.

## 4. Clases de Caracteres y Atajos

### 4.1 Clases de Caracteres

Las clases de caracteres te permiten especificar un conjunto de caracteres entre corchetes `[]`. Por ejemplo:

- `[aeiou]`: Coincide con cualquier vocal.
- `[0-9]`: Coincide con cualquier dígito.
- `[a-zA-Z]`: Coincide con cualquier letra mayúscula o minúscula.

### 4.2 Atajos

Los atajos son secuencias de escape que coinciden con clases predefinidas de caracteres comunes. Algunos atajos comunes incluyen:

- `\d`: Coincide con cualquier dígito (equivalente a `[0-9]`).
- `\D`: Coincide con cualquier carácter que no sea un dígito.
- `\w`: Coincide con cualquier carácter de palabra (letras, dígitos, guiones bajos).
- `\W`: Coincide con cualquier carácter que no sea un carácter de palabra.
- `\s`: Coincide con cualquier carácter de espacio en blanco (espacios, tabulaciones, nuevas líneas).
- `\S`: Coincide con cualquier carácter que no sea un espacio en blanco.

**Ejemplos:**
- `\d{3}` coincidirá con tres dígitos.
- `[aeiou]` coincidirá con cualquier vocal.
- `\w+` coincidirá con una o más letras, dígitos o guiones bajos.

## 5. Grupos y Capturas

### 5.1 Creación de Grupos con Paréntesis

En regex, puedes usar paréntesis `()` para crear grupos. Los grupos son útiles para aplicar cuantificadores a partes específicas de tu patrón.

**Ejemplo:**
- `(ab)+` coincidirá con "ab", "abab", "ababab", etc.

### 5.2 Capturar Grupos con ()

Cuando usas paréntesis para crear grupos, también puedes capturar la coincidencia del grupo para su posterior uso.

**Ejemplo:**
```python
import re

patron = "(\d{2})/(\d{2})/(\d{4})"
cadena = "01/12/2023"

# Usamos re.search() para buscar el patrón y capturar los grupos
resultado = re.search(patron, cadena)

# Accedemos a los grupos capturados
if resultado:
    dia, mes, anio = resultado.groups()
    print(f"Día: {dia}, Mes: {mes}, Año: {anio}")
else:
    print("No se encontró una coincidencia.")
```

En este ejemplo, el patrón busca una fecha en formato "dd/mm/yyyy" y captura el día, mes y año en grupos separados.

## 6. Operadores de Alternancia y Anidamiento

### 6.1 Uso de | para la Alternancia

El operador de alternancia `|` permite especificar múltiples alternativas. Por ejemplo:

- `gato|perro` coincidirá con "gato" o "perro".

### 6.2 Anidamiento de Grupos

Puedes anidar grupos para crear patrones más complejos.

**Ejemplo:**
```python
import re

patron = "(gato|perro) (blanco|negro)"
cadena = "gato blanco"

# Usamos re.search() para buscar el patrón y capturar los grupos
resultado = re.search(patron, cadena)

# Accedemos a los grupos capturados
if resultado:
    animal, color = resultado.groups()
    print(f"Animal: {animal}, Color: {color}")
else:
    print("No se encontró una coincidencia.")
```

En este ejemplo, el patrón busca la combinación de "gato" o "perro" seguido de "blanco" o "negro".

### 6.3 Uso de Grupos Anónimos `(?:...)`

Los grupos anónimos `(?:...)` permiten agrupar sin capturar, útiles cuando no necesitas recuperar la información capturada.

**Ejemplo:**
```python
import re

patron = "(gato|perro) (?:blanco|negro)"
cadena = "perro blanco"

# Usamos re.search() para buscar el patrón y capturar los grupos
resultado = re.search(patron, cadena)

# Accedemos a los grupos capturados
if resultado:
    animal = resultado.group(1)
    print(f"Animal: {animal}")
else:
    print("No se encontró una coincidencia.")
```

En este caso, solo se captura el tipo de animal, ignorando el color.

## 7. Funciones de Regex en Python

### 7.1 Importar el Módulo `re`

Para utilizar expresiones regulares en Python, necesitas importar el módulo `re`.

```python
import re
```

Este módulo proporciona funciones esenciales para trabajar con expresiones regulares.

### 7.2 Funciones Principales

A continuación, se presentan algunas de las funciones más utilizadas del módulo `re`:

- `re.match(patron, cadena)`: Busca el patrón solo al principio de la cadena.

- `re.search(patron, cadena)`: Busca el patrón en cualquier parte de la cadena.

- `re.findall(patron, cadena)`: Encuentra todas las ocurrencias del patrón en la cadena y devuelve una lista.

- `re.finditer(patron, cadena)`: Similar a `findall`, pero devuelve un iterador.

- `re.sub(patron, reemplazo, cadena)`: Sustituye las ocurrencias del patrón con el texto de reemplazo.

- `re.fullmatch(patron, cadena)`: Busca el patrón en toda la cadena y devuelve un objeto de coincidencia si la cadena completa coincide con el patrón.

- `re.split(patron, cadena)`: Divide la cadena en una lista utilizando el patrón como delimitador.

- `re.escape(cadena)`: Escapa caracteres especiales en la cadena para que puedan coincidir literalmente en un patrón.

- `re.compile(patron)`: Compila un patrón de expresión regular en un objeto de patrón, lo que permite un uso más eficiente cuando se realiza la misma búsqueda en varias ocasiones.

### 7.3 Uso de la Notación `r""`

La notación `r""` (raw string) en Python se utiliza comúnmente con expresiones regulares para evitar el escape automático de caracteres especiales. Por ejemplo:

```python
patron = r"\d{3}-\d{2}-\d{4}"
```

Aquí, `\d` representa un dígito, y el prefijo `r` indica que la cadena es una cadena cruda, lo que significa que los caracteres de barra invertida se toman literalmente.

### Ejemplos de Funciones de Regex en Python

Vamos a ver ejemplos prácticos de cada una de las funciones mencionadas:

#### 1. `re.match(patron, cadena)`

```python
import re

patron = r"\d{3}"
cadena = "123abc"

resultado = re.match(patron, cadena)

if resultado:
    print("Coincidencia encontrada al principio de la cadena:", resultado.group())
else:
    print("No se encontró una coincidencia al principio de la cadena.")
```

#### 2. `re.search(patron, cadena)`

```python
import re

patron = r"\d{3}"
cadena = "abc123def"

resultado = re.search(patron, cadena)

if resultado:
    print("Coincidencia encontrada en cualquier parte de la cadena:", resultado.group())
else:
    print("No se encontró una coincidencia en cualquier parte de la cadena.")
```

#### 3. `re.findall(patron, cadena)`

```python
import re

patron = r"\d{3}"
cadena = "123abc456def789"

resultado = re.findall(patron, cadena)

if resultado:
    print("Coincidencias encontradas:", resultado)
else:
    print("No se encontraron coincidencias.")
```

#### 4. `re.finditer(patron, cadena)`

```python
import re

patron = r"\d{3}"
cadena = "123abc456def789"

iterador = re.finditer(patron, cadena)

for resultado in iterador:
    print("Coincidencia encontrada:", resultado.group())
```

#### 5. `re.sub(patron, reemplazo, cadena)`

```python
import re

patron = r"\d{3}"
cadena = "123abc456def789"

cadena_modificada = re.sub(patron, "XXX", cadena)

print("Cadena modificada:", cadena_modificada)
```

#### 6. `re.fullmatch(patron, cadena)`

```python
import re

patron = r"\d{3}"
cadena = "123"

resultado = re.fullmatch(patron, cadena)

if resultado:
    print("La cadena completa coincide con el patrón:", resultado.group())
else:
    print("La cadena no coincide completamente con el patrón.")
```

#### 7. `re.split(patron, cadena)`

```python
import re

patron = r"\s+"
cadena = "Python es un lenguaje de programación"

palabras = re.split(patron, cadena)

print("Palabras separadas:", palabras)
```

#### 8. `re.escape(cadena)`

```python
import re

cadena = "www.example.com"

patron = re.escape("www.example.com")

resultado = re.search(patron, cadena)

if resultado:
    print("Coincidencia encontrada:", resultado.group())
else:
    print("No se encontró una coincidencia.")
```

#### 9. `re.compile(patron)`

```python
import re

patron = re.compile(r"\d{3}")

cadena1 = "123abc"
cadena2 = "456def"

resultado1 = patron.search(cadena1)
resultado2 = patron.search(cadena2)

if resultado1:
    print("Coincidencia encontrada en la cadena1:", resultado1.group())
else:
    print("No se encontró una coincidencia en la cadena1.")

if resultado2:
    print("Coincidencia encontrada en la cadena2:", resultado2.group())
else:
    print("No se encontró una coincidencia en la cadena2.")
```
