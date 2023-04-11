#Lote version python v1
import time
from classes.Historico import Historico
from utils.db import Database
from utils.excel import Excel
from variables import *
from utils.writeFile import File 
from datetime import datetime
import os

db = Database
cnxn = db.conectar()
resultado = []
ahora = datetime.now()
strDate = ahora.strftime("%y%m%d")
strDate = "230301"  # Test specific date
control = excelControl = 0
print(strDate)

i = 0
if (cnxn):
  print("conected DB")
  if (control == 0):
    result = Historico.getHistoricoPagoList(strDate, cnxn) # Get Historico

    if(len(result)):
      #Generate excel from Historico
      Excel.make_report_excel(result, nroAfiliado)

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

      fecha = datetime.strptime(strDate, "%y%m%d")

      date = datetime.now().replace(year=fecha.year, month=fecha.month, day=fecha.day)

      print('Hoy', ahora)
      print('Dia que se corrio', date)

      #Ficheros
      nombre_archivo_bangente = fecha.strftime("%Y%m%d") + "PAGO"
      fichero = os.path.join(rutaArchivo, nombre_archivo_bangente + ".txt")
      # archivo_xls = os.path.join(ruta_archivo, nombre_archivo + ".xls")
      log = os.path.join(rutaArchivo, "logApp.txt")

      print("Nombre archivo", nombre_archivo_bangente)

      if os.path.exists(fichero):
        os.remove(fichero)
      if not os.path.exists(log):
        open(log, "w").close()

      line0 = line1 = ""

      #Generate Archivo for banc txt
      File.writeFile(result, date, fichero, numeroLote, nombre_archivo, cnxn)
    else:
      print("No hay registros")
else:
  print("error contect")


#Init install with python, pip
# pip install pyodbc
# pip install openpyxl 
