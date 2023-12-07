import re
import datetime
import pandas as pd

# Crea las fechas ingresadas por el usuario en objetos datetime para representar las fechas de forma mas estructurada
def verificar_fechas(fecha_inicio_str, fecha_fin_str):
    fecha_inicio = datetime.datetime.strptime(fecha_inicio_str, '%d/%m/%Y')
    fecha_fin = datetime.datetime.strptime(fecha_fin_str, '%d/%m/%Y')

     # Verificar que la fecha de inicio no sea posterior a la fecha de fin
    if fecha_inicio > fecha_fin:
        raise ValueError("La fecha de inicio no puede ser posterior a la fecha de fin.")

    return fecha_inicio, fecha_fin

# Función para determinar si una fecha es un día laborable
def es_dia_laborable(fecha):
    return fecha.weekday() in [0, 1, 2, 3, 4]  # 0=Lunes, 1=Martes, ...


def procesar_archivo(fecha_inicio, fecha_fin):
    # Expresión regular para dividir cada línea del registro en campos, grupo de capturas
    patron = re.compile(r'(?P<ID>[^;]+);(?P<Usuario>[^;]+);(?P<Inicio>[^;]+);(?P<Fin>[^;]+);(?P<Session>[^;]+);(?P<Input>[^;]+);(?P<Output>[^;]+);(?P<MAC_AP>[^;]+);(?P<MAC_Cliente>[^;]+)')

    resultados = []
    se_encontraron_registros = False

    with open('logs.txt', 'r') as archivo:
        next(archivo)  # Ignorar la primera línea (encabezados)
        
        print('Espere, el archivo se está procesando...')
        
        for linea in archivo:
            coincidencias = patron.match(linea)
            if coincidencias:
                campos = coincidencias.groupdict()
                fecha_registro = datetime.datetime.strptime(campos['Inicio'], '%d/%m/%Y %H:%M')

                # Verificar si el dia es laborable y ver si la fecha_registro esta dentro del rango proporcionado
                if es_dia_laborable(fecha_registro) and fecha_inicio.date() <= fecha_registro.date() <= fecha_fin.date():
                    resultados.append(campos)
                    se_encontraron_registros = True

    if not se_encontraron_registros:
        print("No se encontraron registros para el rango de fechas proporcionado.")

    return resultados

def exportar_resultados(resultados):
    # Crear un DataFrame a partir de la lista de resultados
    columnas = ['ID', 'Usuario', 'Inicio', 'Fin', 'Session', 'Input', 'Output', 'MAC_AP', 'MAC_Cliente']
    resultados_df = pd.DataFrame(resultados, columns=columnas)
    
    print('Espere, exportando resultados a usuarios_conectados.xlsx...')
    
    resultados_df.to_excel('usuarios_conectados.xlsx', index=False)
    print("El análisis se ha completado y los resultados se han guardado en 'usuarios_conectados.xlsx'.")

def main():
    try:
        # Obtener la fecha de inicio y fin ingresadas por el usuario
        fecha_inicio_str = input("Ingrese la fecha de inicio (dd/mm/yyyy): ")
        fecha_fin_str = input("Ingrese la fecha de fin (dd/mm/yyyy): ")

        fecha_inicio, fecha_fin = verificar_fechas(fecha_inicio_str, fecha_fin_str)
        resultados = procesar_archivo(fecha_inicio, fecha_fin)
        exportar_resultados(resultados)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Se ha producido un error inesperado: {e}")

if __name__ == "__main__":
    main()
