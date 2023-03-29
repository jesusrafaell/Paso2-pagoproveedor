from classes.LoteBanco import LotesBanco
from variables import *
from datetime import datetime
from classes.Historico import Historico
from utils.utilitis import Util
from classes.LoteDetalle import LoteDetalle
from utils.db import Database as db
from typing import List
import os

class File:
  def writeFile(arr: List[Historico], ahora: datetime, fichero: str, numeroLote: int, nombre_archivo:str, cnxn):
    if not os.path.exists(fichero):
      with open(fichero, "w") as file:
          formatted_time = ahora.strftime("%H%M%S")
          formatted_date = ahora.strftime('%Y%m%d')

          id_proceso = formatted_date + formatted_time + "000000000003".rjust(12, "0") + "019" + "000"
          # Get montototal del archivo
          montoTotal = 0
          comerRif, nroCuentaBanco = Util.get_dataBanco(arr)

          for registro in arr:
              # comerRif = registro.comerRifBanco;
              # nroCuentaBanco = registro.aboNroCuentaBanco;
              montoTotal += registro.hisAmountTotal
          
          # print(nroCuentaBanco, comerRif)

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
              + nroCuentaBanco.rjust(20, "0") 
              + comerRif.rjust(20, "0") 
              + str(montoTotal).replace(",", "").replace(".", ",").rjust(23, "0") 
              + str(montoTotal).replace(",", "").replace(".", ",").rjust(23, "0") 
              + str(len(arr)).rjust(6, "0") 
              + "00" 
              + nombre_archivo.rjust(30, "0")
          ) 
          # print(line0)
          file.write(line0 + "\r")

          cont = 1
          for registro in arr:

            loteDetalle5 = LoteDetalle()

            montoTotal = registro.hisAmountTotal
            id_proceso = formatted_date + formatted_time + "000000000003".rjust(12, "0") + "019" + "000"
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

            cont += 1
            #save LoteDetalle4
            # loteDetalle4.lotCodCompania ="D0U"
            # loteDetalle4.lotNumLote = nombre_archivo
            # loteDetalle4.lotNumPagoProveedor = registro.hisId
            # loteDetalle4.lotTipoRegistro = 4
            # loteDetalle4.lotEmailBeneficiario=registro.contMail
            # loteDetalle4.lotRifBeneficiario = registro.comerRif
            # loteDetalle4.lotMontoTotal = registro.hisAmountTotal

            #Linea 1 save
            loteDetalle4 = LoteDetalle.init__line1(
              "D0U", 
              nombre_archivo, 
              registro.hisId,
              4,
              registro.contMail,
              registro.comerRif,
              registro.hisAmountTotal
            )

            db.saveLoteDetalle(loteDetalle4, cnxn)

            tipoCuentaAbono = Util.getTipoCuentaAbono(registro.aboCodBanco)

            lotConceptoPago = ("Abono por concepto " + afiliado + " comercio: "
                    + registro.comerDesc.strip()
                    + " " + registro.hisLote.strip() + " "
                    + registro.aboTerminal.strip() + " "
                    + str(registro.hisFecha.strftime("%Y-%m-%d"))+ "");

            #Linea 2 save
            loteDetalle5 = LoteDetalle.init__line2(
              "D0U", 
              nombre_archivo, 
              registro.hisId,
              5,
              registro.hisAmountTotal,
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
            db.saveLoteDetalle(loteDetalle5, cnxn)
            
            file.write(line1 + "\r")
          #end for

          formatted_cabecera = ahora.strftime('%Y-%m-%d')
          loteCabecera = LotesBanco()
          loteCabecera.lotActividadEcom = 00
          loteCabecera.lotCantidadPagos =cont 
          loteCabecera.lotCodCompania ="D0U"
          loteCabecera.lotCodMonedaCred = "VES"
          loteCabecera.lotCodMonedaDeb = "VES"
          loteCabecera.lotCuentaDebito = cuentaDebito
          loteCabecera.lotFechaValor = formatted_cabecera
          loteCabecera.lotMontoTotal = montoTotal
          loteCabecera.lotMotivoOpe = 000
          loteCabecera.lotNumLote = nombre_archivo
          loteCabecera.lotTipoRegistro = 9
          db.saveLoteCabecera(loteCabecera, nroAfiliado, cnxn)
    else: 
          print("error writeFile")