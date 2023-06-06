import time
from classes.Historico import Historico
from utils.excel import Excel
from utils.sftp import sftp
from variables import *
from utils.writeFile import File 
from datetime import datetime
import os
from utils.db import Database as db
import sys


agregador = sys.argv[1];
generar = int(sys.argv[2] if len(sys.argv) > 2 else 0)
server = ''
database = ''
username = ''
password = ''
rutaArchivo = ''
nroAfiliado = ''
if agregador.lower() == 'milpagos':
  server = server_m
  database = database_m
  username = username_m
  password = password_m
  rutaArchivo = rutaArchivo_m
elif agregador.lower() == 'carropago': 
  server = server_c
  database = database_c
  username = username_c
  password = password_c
  rutaArchivo = rutaArchivo_c
else:
  print('No existe ese agregador')
  sys.exit()
print(server, database, username, password)
cnxn = db.conectar(server, database, username, password)
resultado = []
ahora = datetime.now()
strDate = ahora.strftime("%y%m%d")
strDateX =  strDate
strDateX = "230604"  # Test specific date 100

print('fecha', strDate)

fecha = datetime.strptime(strDate, "%y%m%d")
date = datetime.now().replace(year=fecha.year, month=fecha.month, day=fecha.day)

# Verificar si la ruta existe y crearla si no
if not os.path.exists(rutaArchivo):
    os.makedirs(rutaArchivo)

#Log
log_file = os.path.join(rutaArchivo, "logApp.txt")
# Crear el archivo si no existe
if not os.path.exists(log_file):
    open(log_file, "w").close()

#Abrir archivo los
log = open(log_file, "a")

if cnxn:
  print("Connected to DB")
  result = Historico.getHistoricoPagoList(strDateX, cnxn) # Get Historico

  print(len(result))

  if len(result):
    print('Number of records: ', len(result))

    #Test
    aux = list(result)
    if generar:
        while len(result) < generar:
          cont = 0
          for registro in result:
            if cont == generar:
              break
            result.append(registro)
            cont += 1
            print('cont de registros', cont)
        print('Generate: ', len(result))

    # Generate excel from Historico
    Excel.make_report_excel(date, result, nroAfiliado, rutaArchivo)

    day = datetime.now().day
    month = datetime.now().month
    dayS = str(day).zfill(2)
    monthS = str(month).zfill(2)

    valueafiliado = reportBeginFile
    lotefile =  str(valueafiliado) + monthS + dayS
    numeroLote = int(db.getNumeroLote("D0U", lotefile, cnxn)) + 1

    print("Lote number: ",  numeroLote)

    nombre_archivo = lotefile + str(numeroLote).zfill(2)

    print('Today:', ahora)
    print('Date that was run:', date)

    #Ficheros
    nombre_archivo_bangente = fecha.strftime("%Y%m%d") + "PAGOS01"
    fichero = os.path.join(rutaArchivo, nombre_archivo_bangente + ".txt")

    print("Nombre archivo", nombre_archivo_bangente)

    if os.path.exists(fichero):
      os.remove(fichero)

    # Generate Archivo for banc txt
    File.writeFile(result, date, fichero, numeroLote, nombre_archivo, cnxn, log)

    # if sftp(fichero, nombre_archivo_bangente + '.txt'):
    #   print('Process completed!!')
    #   log.write(datetime.now() + " Error: " + 'Process completed!!' + "\n")
    # else:
    #   print('Process error SFTP!!')
    #   log.write(datetime.now() + " Error: " + "Process error SFTP!!" + "\n")
  else:
    print("No existen registros")
    log.write(str(strDate + " Error: " + "No records found" + "\n"))
else:
  print("Error connecting to DB")
  log.write(datetime.now() + "Error connecting to DB" + "No records found" + "\n")
log.close()
