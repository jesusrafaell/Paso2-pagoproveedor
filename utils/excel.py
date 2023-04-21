from typing import List
from datetime import datetime
from variables import *
import openpyxl
from utils.utilitis import Util

from classes.Historico import Historico

class Excel:
  def make_report_excel(date: datetime, resultList: List[Historico], afiliado: str):
    # print('make_report_excel')
    fecha = date.strftime("%Y%m%d") 
    fileName = rutaArchivo + "\\" + fecha + ".xlsx"
    hoja = "ArchivoPagoComercios"

    header = ["Numero Pago a Proveedor", "RIF", "Beneficiario", "Banco Beneficiario", "Cuenta Beneficiario", "Concepto", "Monto", "Terminal"]
    title = "ArchivoPagoAComercios"

    try:
        write_excel(resultList, header, fileName,  title, hoja, afiliado)
    except Exception as e:
        print(e)

def write_excel(data: List[Historico], header, filename, title, sheetname, afiliado):
    try:
        print('write_excel')
        wb = openpyxl.Workbook()
        # Seleccionar la hoja activa
        sheet = wb.active

        #guardar header
        # print(header)
        sheet.append(header)

        #guardar rows
        for registro in data:
            row = [
               Util.leftPad(str(registro.hisId), 8, '0'),
               str(registro.comerRif), 
               registro.comerDesc.strip(),
               registro.aboCodBanco,
               registro.aboNroCuenta,
               "Abono por concepto MilPagos comercio: " + 
                registro.comerRif.strip() + " " + 
                registro.hisLote.strip() + " " + 
                registro.aboTerminal.strip() + " " + 
                str(registro.hisFecha),
               registro.hisAmountTotal,
               registro.aboTerminal
               ]
            # print(row)
            sheet.append(row)

        # print('Nombre archivo excel:', filename)
        wb.save(filename)

    except Exception as e:
        print(e)