import decimal

class Historico:
    
    def __init__(self):
        self.hisId = None
        self.aboCodAfi = None
        self.aboCodComercio = 0
        self.aboTerminal = None
        self.aboCodBanco = None
        self.aboNroCuenta = None
        self.aboNroCuentaBanco = None
        self.aboTipoCuenta = None
        self.comerDesc = None
        self.comerTipoPer = 0
        self.comerPagaIva = None
        self.comerCodUsuario = None
        self.comerCodPadre = 0
        self.comerRif = None
        self.comerRifBanco = None
        self.contNombres = None
        self.contApellidos = None
        self.contTelefLoc = None
        self.contTelefMov = None
        self.contMail = None
        self.afiDesc = None
        self.afiCodTipoPer = 0
        self.hisLote = None
        self.hisRecordTDD = 0
        self.hisAmountTDD = 0.0
        self.hisRecordTDC = 0
        self.hisAmountTDC = 0.0
        self.hisAmountTDCImpuesto = 0.0
        self.hisAmountIVA = 0.0
        self.hisAmountComisionBanco = 0.0
        self.hisAmountTotal = None
        self.hisFecha = None
        self.hisFechaProceso = None
        self.hisFechaEjecucion = None

    def __str__(self):
        return f"Historico(id={self.hisId} aboCodAfi={self.aboCodAfi}, aboCodComercio={self.aboCodComercio}, aboTerminal={self.aboTerminal}, aboCodBanco={self.aboCodBanco}, aboNroCuenta={self.aboNroCuenta}, aboTipoCuenta={self.aboTipoCuenta}, comerDesc={self.comerDesc}, comerTipoPer={self.comerTipoPer}, comerPagaIva={self.comerPagaIva}, comerCodUsuario={self.comerCodUsuario}, comerCodPadre={self.comerCodPadre}, comerRif={self.comerRif}, contNombres={self.contNombres}, contApellidos={self.contApellidos}, contTelefLoc={self.contTelefLoc}, contTelefMov={self.contTelefMov}, contMail={self.contMail}, afiDesc={self.afiDesc}, afiCodTipoPer={self.afiCodTipoPer}, hisLote={self.hisLote}, hisRecordTDD={self.hisRecordTDD}, hisAmountTDD={self.hisAmountTDD}, hisRecordTDC={self.hisRecordTDC}, hisAmountTDC={self.hisAmountTDC}, hisAmountTDCImpuesto={self.hisAmountTDCImpuesto}, hisAmountIVA={self.hisAmountIVA}, hisAmountComisionBanco={self.hisAmountComisionBanco}, hisAmountTotal={self.hisAmountTotal}, hisFecha={self.hisFecha}, hisFechaProceso={self.hisFechaProceso}, hisFechaEjecucion={self.hisFechaEjecucion})"
        
    def getHistoricoPagoList(fecha: str, cnxn):
        SPsql = "EXEC SP_consultaHistoricoPago_BGENTE ?, ?"
        params = (fecha, '1')
        cursor = cnxn.cursor().execute(SPsql, params)

        # print('__________________________________________________\n')

        # Obtener los nombres de las columnas
        column_names = [column[0] for column in cursor.description]

        # Recorrer todos los resultados y crear un diccionario para cada uno
        results = []
        while True:
            result = cursor.fetchone()
            if result is None:
                break
            result_dict = {}
            for i in range(len(column_names)):
                result_dict[column_names[i]] = result[i]
            results.append(result_dict)
        
        # Imprimir la lista de resultados en formato clave: valor
        historicos = []
        for row in results:
            historico = Historico()
            historico.hisId = row['hisId']
            historico.aboCodAfi = row['aboCodAfi']
            historico.aboCodComercio = row['aboCodComercio']
            historico.aboTerminal = row['aboTerminal']
            historico.hisLote = row['hisLote']
            historico.hisRecordTDD = row['hisRecordTDD']
            historico.hisRecordTDC = row['hisRecordTDC']
            historico.hisAmountTDD = row['hisAmountTDD']
            historico.hisAmountTDC = row['hisAmountTDC']
            historico.hisAmountTDCImpuesto = row['hisAmountTDCImpuesto']
            historico.hisAmountIVA = row['hisAmountIVA']
            historico.hisAmountComisionBanco = row['hisAmountComisionBanco']
            historico.hisAmountTotal = row['hisAmountTotal']
            historico.hisFechaEjecucion = row['hisFechaEjecucion']
            historico.hisFecha = row['hisFechaEjecucion']
            historico.hisFechaProceso = row['hisFechaProceso']
            historico.aboCodBanco = row['comerCodigoBanco']
            historico.aboNroCuenta = row['comerCuentaBanco']
            historico.aboNroCuentaBanco = row['aboNroCuenta']
            historico.aboTipoCuenta = row['aboTipoCuenta']
            historico.comerDesc = row['comerDesc']
            historico.comerTipoPer = row['comerTipoPer']
            historico.comerPagaIva = row['comerPagaIva']
            historico.comerCodUsuario = row['comerCodUsuario']
            historico.comerRif = row['comerRifCliente']
            historico.comerRifBanco = row['comerRif']
            historico.contNombres = row['contNombres']
            historico.contApellidos = row['contApellidos']
            historico.contTelefLoc = row['contTelefLoc']
            historico.contTelefMov = row['contTelefMov']
            historico.contMail = row['contMail']
            historico.afiDesc = row['afiDesc']
            historico.afiCodTipoPer = row['afiCodTipoPer']
            historico.comerCodPadre = row['comerCodPadre']

            historicos.append(historico)

        return historicos