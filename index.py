import time
from classes.Historico import Historico
from utils.excel import Excel
from utils.sftp import sftp
from variables import *
from utils.writeFile import File 
from datetime import datetime
import os
from utils.db import Database as db

cnxn = db.conectar()
resultado = []
ahora = datetime.now()
strDate = ahora.strftime("%y%m%d")
#Test SP
strDateX = "230428"  # Test specific date

#Test
# strDate = "230503"
# ahora= datetime.strptime("230503", "%y%m%d")
##############

control = excelControl = 0
print(strDate)

fecha = datetime.strptime(strDate, "%y%m%d")
date = datetime.now().replace(year=fecha.year, month=fecha.month, day=fecha.day)

#Log
log = os.path.join(rutaArchivo, "logApp.txt")
if not os.path.exists(log):
  open(log, "w").close()

if cnxn:
  print("Connected to DB")
  result = Historico.getHistoricoPagoList(strDateX, cnxn) # Get Historico

  print(len(result))

  if len(result):
    print('Number of records: ', len(result))

    #Test
    aux = list(result)
    while len(result) < 500:
        result.extend(aux)
    print('Generate: ', len(result))

    # Generate excel from Historico
    Excel.make_report_excel(date, result, nroAfiliado)

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
    print("No records found")
    log.write(str(datetime.now()) + " Error: " + "No records found" + "\n")
else:
  print("Error connecting to DB")
  log.write(datetime.now() + "Error connecting to DB" + "No records found" + "\n")
