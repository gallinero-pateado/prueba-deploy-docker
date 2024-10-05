print("Hola mundo");

nombre_archivo = 'output.txt'

contenido = 'Hola, este es un archivo de texto generado por python.'

with open (nombre_archivo, 'w') as archivo:
    archivo.write(contenido)

print(f'Archivo "{nombre_archivo}" creado con éxito.')
