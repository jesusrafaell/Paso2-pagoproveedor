#Lote version python v1
import decimal
import time
from classes.Historico import Historico
from utils.db import Database
from variables import *
from utils.writeFile import File 
from datetime import datetime
import os

db = Database
cnxn = db.conectar()
ahora = datetime.now()
# montoTotal = decimal.Decimal(0)
# montoTotal = montoTotal.quantize(decimal.Decimal('0.01'), rounding=decimal.ROUND_CEILING)
resultado = []
strDate = time.strftime("%y%m%d")
strDate = "230301"  # Test specific date
control = excelControl = 0
print(strDate)

i = 0
# while i < 1:
if (cnxn):
  print("conected DB")
  if (control == 0):
    result = Historico.getHistoricoPagoList(strDate, cnxn) # Get Historico

    print("Cantidad Resgistros ",  len(result))

    day = datetime.now().day
    month = datetime.now().month

    dayS = str(day).zfill(2)
    monthS = str(month).zfill(2)

    valueafiliado = reportBeginFile
    lotefile =  str(valueafiliado) + monthS + dayS
    numeroLote = int(db.getNumeroLote("D0U", lotefile, cnxn)) + 1

    print("lote---> ",  numeroLote)

    nombre_archivo = lotefile + str(numeroLote).zfill(2)

    fecha = datetime.now().strftime("%Y%m%d")

    #Ficheros
    nombre_archivo_bangente = fecha + "PAGO"
    ruta_archivo = rutaArchivo
    fichero = os.path.join(ruta_archivo, nombre_archivo_bangente + ".txt")
    archivo_xls = os.path.join(ruta_archivo, nombre_archivo + ".xls")
    log = os.path.join(rutaArchivo, "logApp.txt")

    print("Nombre archivo", nombre_archivo_bangente)

    if os.path.exists(fichero):
      os.remove(fichero)
    if os.path.exists(archivo_xls):
      os.remove(archivo_xls)
    if not os.path.exists(log):
      open(log, "w").close()

    if(len(result)):
      line0 = line1 = ""
      File.writeFile(result, ahora, fichero, numeroLote, nombre_archivo, cnxn)
else:
  print("error contect")