from classes.LoteBanco import LotesBanco
from variables import *
from classes.LoteDetalle import LoteDetalle
import pyodbc

class Database:
    
    def __init__(self):
        self.codigoError = ""
        self.descripcionError = ""	
        self.conn = None                
        self.entrada = None
    

    def conectar():
        try:		
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos", e)
            return None

    def getCuentaBanco(cnxn):
        SPsql = "EXEC GetCuentaBanco"
        result = cnxn.cursor().execute(SPsql)
        row = result.fetchone()
        # print (row[0])
        return row[0]

    def getNumeroLote(compania,fecha ,cnxn):
        sql = "select ISNULL( MAX(SUBSTRING(lotNumLote,7,2)) , 0) as lote from Lotesxbanco where lotCodCompania = ? and SUBSTRING(lotNumLote,1,6) = ?"
        params = (compania, fecha)
        result = cnxn.cursor().execute(sql, params)
        res = result.fetchone()
        return res[0]


    def saveLoteDetalle(lote: LoteDetalle, cnxn): 
        stmt = (
              "INSERT INTO LotesDetalle (lotCodCompania, lotNumLote, lotTipoRegistro, lotCodMonedaDeb, "
            + "lotCodMonedaCred, lotActividadEcom, lotMotivoOpe, lotCuentaDebito, lotFechaValor, lotMontoTotal, lotCantidadPagos, lotNumPagoProveedor, "
            + "lotNumFactura, lotEmailBeneficiario, lotRifBeneficiario, lotNombreBeneficiario, lotMonto, lotTipoPago, "
            + "lotCodOficBanco, lotCuentaBeneficiario, lotConceptoPago, lotCodBancoBenef, lotTipoCodBanco, lotNombreBancoBenef, "
            + "lotDireccionBancoBenef)"
            + " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        )
        params = (
            lote.lotCodCompania, 
            lote.lotNumLote, 
            lote.lotTipoRegistro, 
            lote.lotCodMonedaDeb, 
            lote.lotCodMonedaCred, 
            lote.lotActividadEcom, 
            lote.lotMotivoOpe, 
            lote.lotCuentaDebito, 
            lote.lotFechaValor, 
            lote.lotMontoTotal, 
            lote.lotCantidadPagos, 
            lote.lotNumPagoProveedor, 
            lote.lotNumFactura, 
            lote.lotEmailBeneficiario, 
            lote.lotRifBeneficiario, 
            lote.lotNombreBeneficiario, 
            lote.lotMonto, 
            lote.lotTipoPago, 
            lote.lotCodOficBanco, 
            lote.lotCuentaBeneficiario, 
            lote.lotConceptoPago, 
            lote.lotCodBancoBenef, 
            lote.lotTipoCodBanco, 
            lote.lotNombreBancoBenef, 
            lote.lotDireccionBancoBenef 
        )

        with cnxn.cursor() as cursor:
            cursor.execute(stmt, params)
            # cnxn.commit()
            # if cursor.rowcount > 0:
            #     print("Inserción realizada con éxito, tipoRegistro:", lote.lotTipoRegistro, "lote:", lote.lotNumLote)
            # else:
            #     print("La inserción ha fallado, tipoRegistro:", lote.lotTipoRegistro, "lote:", lote.lotNumLote)

        # print("lote save", cursor)


    def saveLoteCabecera(lote: LotesBanco, afiliado: str, cnxn): 
        stmt = (
            "INSERT INTO LotesXbanco (lotCodCompania, lotNumLote, lotTipoRegistro, lotCodMonedaDeb, "
            + "lotCodMonedaCred, lotActividadEcom, lotMotivoOpe, lotCuentaDebito, lotFechaValor, lotMontoTotal, lotCantidadPagos, lotAfiliado, lotTipoArchivo,lotBanco)"
            + " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,1,0104)"
        )
        params = (
            lote.lotCodCompania, 
            lote.lotNumLote,
            lote.lotTipoRegistro,
            lote.lotCodMonedaDeb,
            lote.lotCodMonedaCred, 
            lote.lotActividadEcom, 
            lote.lotMotivoOpe, 
            lote.lotCuentaDebito, 
            lote.lotFechaValor, 
            lote.lotMontoTotal, 
            lote.lotCantidadPagos, 
            afiliado, 
        )

        with cnxn.cursor() as cursor:
            cursor.execute(stmt, params)
            # cnxn.commit()
            # if cursor.rowcount > 0:
            #     print("Inserción realizada con éxito cabezera",  "lote:", lote.lotNumLote)
            # else:
            #     print("La inserción ha fallado cabbezera", "lote:", lote.lotNumLote)

        # print("lote save", cursor)