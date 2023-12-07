import re
import datetime
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Función para realizar el análisis
def analizar_registros():
    # Obtener la fecha de inicio y fin ingresadas por el usuario
    fecha_inicio_str = fecha_inicio_entry.get()
    fecha_fin_str = fecha_fin_entry.get()

    try:
        fecha_inicio = datetime.datetime.strptime(fecha_inicio_str, '%d/%m/%Y')
        fecha_fin = datetime.datetime.strptime(fecha_fin_str, '%d/%m/%Y')

        # Solicitar al usuario seleccionar un archivo
        archivo_path = filedialog.askopenfilename()

        # Función para determinar si una fecha es un día laborable
        def es_dia_laborable(fecha):
            return fecha.weekday() in [0, 1, 2, 3, 4]  # 0=Monday, 1=Tuesday, ...

        # Expresión regular para dividir cada línea del registro en campos
        patron = re.compile(r'(?P<ID>[^;]+);(?P<Usuario>[^;]+);(?P<Inicio>[^;]+);(?P<Fin>[^;]+);(?P<Session>[^;]+);(?P<Input>[^;]+);(?P<Output>[^;]+);(?P<MAC_AP>[^;]+);(?P<MAC_Cliente>[^;]+)')

        # Crear una lista para almacenar los resultados
        resultados = []

        # Leer el archivo de registros
        with open(archivo_path, 'r') as archivo:
            # Ignorar la primera línea (encabezados)
            next(archivo)

            for linea in archivo:
                coincidencias = patron.match(linea)
                if coincidencias:
                    campos = coincidencias.groupdict()
                    fecha_inicio = datetime.datetime.strptime(campos['Inicio'], '%d/%m/%Y %H:%M')

                    if es_dia_laborable(fecha_inicio) and fecha_inicio >= fecha_inicio and fecha_inicio <= fecha_fin:
                        resultados.append(campos)

        # Crear un DataFrame a partir de la lista de resultados
        resultados_df = pd.DataFrame(resultados)

        # Mostrar una ventana temporal que indique que el análisis está en proceso
        ventana_temporal = tk.Toplevel(ventana)
        ventana_temporal.title("Procesando...")

        mensaje_proceso = tk.Label(ventana_temporal, text="El análisis está en proceso. Por favor, espere...", font=("Roboto Mono", 12))
        mensaje_proceso.pack(pady=10)

        ventana_temporal.update()

        # Exportar los resultados a un archivo Excel
        resultados_df.to_excel('usuarios_conectados.xlsx', index=False)

        # Cerrar la ventana temporal
        ventana_temporal.destroy()

        messagebox.showinfo("Finalizado", "El análisis se ha completado y los resultados se han guardado en 'usuarios_conectados.xlsx'")
    except ValueError:
        messagebox.showerror("Error", "Ingrese fechas válidas con el formato 'dd/mm/yyyy'")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Análisis de Registros Wi-Fi")

# Personalizar la fuente
fuente_personalizada = ("Roboto Mono", 12)

# Crear un título con fuente personalizada
titulo = tk.Label(ventana, text="Análisis de Registros Wi-Fi", font=fuente_personalizada)
titulo.pack(pady=10)

# Etiqueta y entrada para la fecha de inicio
fecha_inicio_label = tk.Label(ventana, text="Fecha de Inicio (dd/mm/yyyy):", font=fuente_personalizada)
fecha_inicio_label.pack()
fecha_inicio_entry = tk.Entry(ventana, font=fuente_personalizada)
fecha_inicio_entry.pack()

# Etiqueta y entrada para la fecha de fin
fecha_fin_label = tk.Label(ventana, text="Fecha de Fin (dd/mm/yyyy):", font=fuente_personalizada)
fecha_fin_label.pack()
fecha_fin_entry = tk.Entry(ventana, font=fuente_personalizada)
fecha_fin_entry.pack()

# Botón para realizar el análisis
analizar_button = tk.Button(ventana, text="Realizar Análisis", command=analizar_registros, font=fuente_personalizada)
analizar_button.pack()

ventana.mainloop()