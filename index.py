#Lote version python v1
import decimal
import time
from classes.Historico import Historico
from utils.db import Database
from variables import *
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

    # for row in result:
    #   print(row.__str__())
    print("Cantidad Resgistros ",  len(result))
    nroCuenta = db.getCuentaBanco(cnxn);
    print("Cuenta: " , nroCuenta)
    # System.out.println("Cuenta " + nroCuenta);

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
      if not os.path.exists(fichero):
        with open(fichero, "w") as file:
            codigo_swift = ""
            formatted_time = ahora.strftime("%H%M%S")
            formatted_date = ahora.strftime('%Y%m%d')

            id_proceso = formatted_date + formatted_time + "000000000003".rjust(12, "0") + "019" + "000"
            # Get montototal del archivo
            montoTotal = 0
            for registro in result:
                montoTotal += registro.hisAmountTotal
            # print("Monto Total:", montoTotal)
            line0 = (
                "1"
                + id_proceso.rjust(32, " ") 
                + "00" 
                + str(numeroLote).rjust(10, "0") 
                + "019" 
                + " ".rjust(10) 
                + " ".rjust(6) 
                + " ".rjust(10) 
                + nroCuenta.rjust(20, "0") 
                + "J00003103756".rjust(20, "0") 
                + str(montoTotal).replace(",", "").replace(".", ",").rjust(23, "0") 
                + str(montoTotal).replace(",", "").replace(".", ",").rjust(23, "0") 
                + str(len(result)).rjust(6, "0") 
                + "00" 
                + nombre_archivo.rjust(30, "0")
            ) 
            # print(line0)
            file.write(line0 + "\r")

            cont = 1
            for registro in result:
              montoTotal = registro.hisAmountTotal
              id_proceso = formatted_date + formatted_time + "000000000003".rjust(12, "0") + "019" + "000"
              tipoDoc = "01"
              rif_prefix = registro.comerRif[0]
              if rif_prefix == "V":
                tipoDoc = "01"
              elif rif_prefix in ["P", "J"]:
                tipoDoc = "02"
              elif rif_prefix == "E":
                tipoDoc = "08"

              conceptoMov =  (
                "MILPAGO "
                + registro.comerRif.strip()
                + " "
                + registro.aboTerminal.strip()
                + " "
                + str(registro.hisFecha.strftime("%Y-%m-%d"))
              )

              line1 = (
                "01"
                + id_proceso.rjust(32)
                + "01"
                + str(cont).rjust(10, "0")
                + str(numeroLote).rjust(10, "0")
                + registro.aboNroCuenta.rjust(20, "0")
                + tipoDoc.rjust(3, "0")
                + registro.comerRif[1:].strip().ljust(15, "0")
                + (registro.contNombres + registro.contApellidos).ljust(40, " ")
                + "D"
                + "0".rjust(6, "0")
                + str(montoTotal).replace(",", "").replace(".", ",").rjust(23, "0")
                + " ".rjust(23)
                + " ".rjust(10)
                + "".rjust(30, "0")
                + conceptoMov.rjust(40)
                + "0"
                + "00"
              )

              file.write(line1 + "\r")
else:
  print("error contect")