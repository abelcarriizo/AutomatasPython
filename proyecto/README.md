# Proyecto de Seguimiento de Usuarios en Red WiFi en Días Laborables

## Introducción:
Este proyecto tiene como objetivo desarrollar una aplicación en Python que permita el seguimiento de usuarios que se han conectado a una red WiFi en días laborables específicos, como lunes, martes, miércoles, jueves y viernes, dentro de un rango de fechas definido. El propósito de esta aplicación es proporcionar una herramienta útil para supervisar la actividad de usuarios en una red WiFi y extraer información relevante para la toma de decisiones.

## Estructura del Archivo de Registros

El archivo de registros sigue la siguiente estructura:

```
ID Conexión único;Usuario;Inicio de Conexión;Fin de Conexión;Session Time;Input Octets;Output Octets;MAC AP;MAC Cliente
```
## Implementación en Python

El proyecto se implementará en Python y hará uso de expresiones regulares mediante el módulo `re`. Se utilizará la biblioteca `datetime` para trabajar con fechas y días de la semana.

## Pasos a Seguir

1. **Leer el archivo de registros:** Abre y lee el archivo que contiene los registros de tráfico de conexiones de Wi-Fi.

2. **Procesar los registros:** Divide cada línea en sus campos correspondientes y accede a la información relevante, como fecha y hora de inicio, día de la semana y nombre de usuario.

3. **Filtrar por días laborables y rango de fechas:** Implementa lógica para filtrar conexiones en los días laborables seleccionados y dentro del rango de fechas especificado.

4. **Seguimiento de Usuarios:** Registra y muestra los usuarios que cumplieron con los criterios en la interfaz de usuario.

5. **Exportar a Excel:** Utiliza `pandas` para crear un DataFrame y exportar los resultados a un archivo Excel.

6. **Documentación y Comentarios:** Documenta el código y proporciona comentarios claros para facilitar la comprensión y el uso de la aplicación.

## Ejecutar el Código

Puedes ejecutar el codigo ejecutando el archivo WiFitracking.py:

```bash
python3 WiFitracking.py
```
O puedes ejecutar WiFiTrackingUI.py este ultimo tiene una interfaz grafica desarrollada con tkinter.

```bash
python3 WiFitrackingUI.py
```
