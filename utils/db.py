from variables import *
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

