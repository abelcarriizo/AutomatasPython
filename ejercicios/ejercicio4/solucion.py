import re    

#Expresiones Regulares
email = r'^\S+@um\.edu\.ar$'
twitter = r'^@[A-Za-z0-9_]{1,15}$'
contraseña = r'^(?=.*[A-Z])(?=.*[a-z]{2,})(?=.*[0-9!@#$%^&*()_+])[A-Za-z0-9!@#$%^&*()_+]{8,}$' #lookhead
url = r'^(http|https):\/\/www\.[a-zA-Z0-9-]+\.[a-z]{2,}\/?$'
ip = r'^(\d{1,3}\.){3}\d{1,3}$'
fecha = r'^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/]\d{4}$'

nombre_archivo = input('Indica el nombre del archivo: ')

try:
  with open(nombre_archivo, 'r') as archivo:
      lineas = archivo.readlines()
      # Validar expresiones
      for linea in lineas:
        
        if 'Email:' in linea:
          print('-' * 20) #Detalle estetico
          email_search = re.search(email, linea.split(":")[1].strip())
          if email_search:
            print(f'Email valido: {email_search.group()}')
          else:
            print(f'Email no valido: {linea.split(":")[1].strip()}')

        if 'Twitter:' in linea:
          twitter_search = re.search(twitter, linea.split(':')[1].strip())
          if twitter_search:
            print(f'Cuenta de twitter: {twitter_search.group()}')
          
        if 'Contraseña:' in linea:
          contraseña_search = re.search(contraseña, linea.split(':')[1].strip())
          if contraseña_search:
            print(f'Contraseña valida: {contraseña_search.group()}')
          else:
            print(f'Contraseña no valido: {linea.split(":")[1].strip()}')
      
        if 'URL:' in linea:
          url_search = re.search(url, linea.split()[2].strip())
          if url_search:
            print(f'URL valido: {url_search.group()}')
          else:
            print(f'URL no valido: {linea.split()[2].strip()}')

        if 'Dirección IP:' in linea:
          ip_search = re.search(ip, linea.split(':')[1].strip())
          if ip_search:
            print(f'Direccion IP valida: {ip_search.group()}')
          else:
            print(f'Direccion IP no valida: {linea.split(":")[1].strip()}')

        if 'Fecha:' in linea:
          fecha_search = re.search(fecha, linea.split(':')[1].strip())
          if fecha_search:
            print(f'Fechas validas: {fecha_search.group()}')
          else:
            print(f'Fecha no valida: {linea.split(":")[1].strip()}')

except FileNotFoundError:
  print(f'El archivo "{nombre_archivo}" no fue encontrado')
except Exception as e:
  print(f'Ocurrio un error: {str(e)}')