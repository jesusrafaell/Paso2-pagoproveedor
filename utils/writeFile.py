from classes.LoteBanco import LotesBanco
from variables import *
from datetime import datetime
from classes.Historico import Historico
from utils.utilitis import Util
from classes.LoteDetalle import LoteDetalle
from utils.db import Database as db
import traceback
from typing import List
import os

# codigoClient = codigoClienteDev #Desarrollo
codigoClient = codigoClienteProd #Prod

class File:
  def getLine0(id_proceso: str,numeroLote: str, nroCuentaBanco: str, comerRif: str, montoTotal: float, nombre_archivo: str, total_registros: str) -> str:
    # print(comerRif, comerRif[1:].strip() )
    return (
      "01"
      + Util.leftPad(id_proceso, 32, ' ')
      + "00" 
      + Util.leftPad(numeroLote, 10, '0') 
      + "019" 
      + " ".rjust(10) 
      + " ".rjust(6) 
      + " ".rjust(10) 
      + Util.leftPad(str(nroCuentaBanco), 20, '0')
      + Util.leftPad(str(comerRif[1:].strip()), 20, '0')
      + Util.leftPad(str(Util.rounder(montoTotal)).replace(",", "").replace(".", ","), 23, '0')
      + Util.leftPad(str(Util.rounder(montoTotal)).replace(",", "").replace(".", ","), 23, '0')
      + Util.leftPad(str(total_registros), 6, '0')
      + "00" 
      + Util.leftPad(str(nombre_archivo), 7, '0') #basado en el excel
    ) 

  def writeFile(arr: List[Historico], ahora: datetime, fichero: str, numeroLote: int, nombre_archivo:str, cnxn, log):
    try:
      if not os.path.exists(fichero):
        with open(fichero, "w") as file:
            formatted_time = ahora.strftime("%H%M%S")
            formatted_date = ahora.strftime('%Y%m%d')

            id_proceso = formatted_date + formatted_time + codigoClient.rjust(12, "0") + "019" + "000"
            # Get montototal del archivo
            comerRif, nroCuentaBanco = Util.get_dataBanco(arr)

            montoTotal = float(0)
            # contx = float(0) + 1

            for registro in arr:
                montoTotal += registro.hisAmountTotal

                # print('-->', registro.hisId, registro.hisAmountTotal)
                # registro.hisAmountTotal = contx
                # montoTotal += contx
                # contx  += 1

                # if registro.hisAmountTotal > 1:
                #   print(montoTotal, 'mayor')
                #   print(registro.hisId,registro.aboTerminal, registro.hisFechaEjecucion, registro.hisFechaProceso)

                # if registro.aboNroCuenta[0:4] == '0146': #si es de bangente
                #   print(registro.hisId,registro.aboTerminal, registro.hisFechaEjecucion, registro.hisFechaProceso)

            # print('Monto toal', montoTotal)
            # print("header",nroCuentaBanco, comerRif)

            # print("Monto Total:", montoTotal)
            line0 = File.getLine0(id_proceso, numeroLote, nroCuentaBanco,comerRif,montoTotal,nombre_archivo,len(arr))
            # print(line0)
            file.write(line0 + "\r")

            cont = 1
            montoTotal = float(0)
            aux = float(0)
            # contx2 = float(0) + 1
            for registro in arr:

              loteDetalle2 = LoteDetalle()

              montoTotal = registro.hisAmountTotal
              aux += montoTotal
              # registro.hisAmountTotal = contx
              # montoTotal += contx2
              # contx  += 1
              # print('2 -->', registro.hisId, montoTotal)
              id_proceso = formatted_date + formatted_time + codigoClient.rjust(12, "0") + "019" + "000"
              tipoDoc = Util.get_rif_prefix(registro.comerRif[0])
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
                + Util.leftPad(str(id_proceso), 32, ' ')
                + "01"
                + Util.leftPad(str(cont), 10, '0')
                + Util.leftPad(str(numeroLote), 10, '0')
                + Util.leftPad(str(registro.aboNroCuenta), 20, '0')
                + Util.leftPad(str(tipoDoc), 3, '0')
                + Util.leftPad(str(registro.comerRif[1:].strip()), 15, '0')
                + Util.rightPad(str( (registro.contNombres + registro.contApellidos)), 40, ' ')
                + "C" #Credito
                + Util.leftPad("0", 6,'0')
                + Util.leftPad(str(Util.rounder(montoTotal)).replace(",", "").replace(".", ","), 23, '0')
                + " ".rjust(23)
                + " ".rjust(10) 
                + "".rjust(30, "0")
                + Util.rightPad(str(conceptoMov), 40,'0')
                + "0"
                + "00"
              )

              # print(Util.leftPad(str(Util.rounder(montoTotal)).replace(",", "").replace(".", ","), 23, '0'))

              cont += 1

              #Linea 1 save
              loteDetalle1 = LoteDetalle.init__line1(
                "D0U", 
                nombre_archivo, 
                registro.hisId,
                4,
                registro.contMail,
                registro.comerRif,
                Util.rounder(registro.hisAmountTotal)
              )

              #inset
              # db.saveLoteDetalle(loteDetalle1, cnxn)

              tipoCuentaAbono = Util.getTipoCuentaAbono(registro.aboCodBanco)

              lotConceptoPago = ("Abono por concepto " + afiliado + " comercio: "
                      + registro.comerDesc.strip()
                      + " " + registro.hisLote.strip() + " "
                      + registro.aboTerminal.strip() + " "
                      + str(registro.hisFecha.strftime("%Y-%m-%d"))+ "");

              #Linea 2 save
              loteDetalle2 = LoteDetalle.init__line2(
                "D0U", 
                nombre_archivo, 
                registro.hisId,
                5,
                Util.rounder(registro.hisAmountTotal),
                registro.comerDesc,
                tipoCuentaAbono,
                registro.aboNroCuentaBanco,
                "VES",
                "VES",
                lotConceptoPago,
                "",
                "BIC",
                000,
                00,
                cuentaDebito
              )

              #inset
              # db.saveLoteDetalle(loteDetalle2, cnxn)
              
              file.write(line1 + "\r")
            #end for

            # print('monto afeter registros', Util.rounder(aux).replace(',','').replace(".", ","))
            formatted_cabecera = ahora.strftime('%Y-%m-%d')
            loteCabecera = LotesBanco()
            loteCabecera.lotActividadEcom = 00
            loteCabecera.lotCantidadPagos =cont 
            loteCabecera.lotCodCompania ="D0U"
            loteCabecera.lotCodMonedaCred = "VES"
            loteCabecera.lotCodMonedaDeb = "VES"
            loteCabecera.lotCuentaDebito = cuentaDebito
            loteCabecera.lotFechaValor = formatted_cabecera
            loteCabecera.lotMontoTotal = Util.rounder(montoTotal)
            loteCabecera.lotMotivoOpe = 000
            loteCabecera.lotNumLote = nombre_archivo
            loteCabecera.lotTipoRegistro = 9
            #inset
            # db.saveLoteCabecera(loteCabecera, nroAfiliado, cnxn)
      else: 
        print("error writeFile")
    except Exception as e:
      # Captura cualquier excepción y escribe el mensaje de error en el archivo log.txt
      print(e)
      error_message = traceback.format_exc()
      log.write("Error: " + str(e) + "\n" + error_message + '\n')
