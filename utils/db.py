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
    
    def conectar(server, database,username, password):
        try:		
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            return conexion
        except Exception as e:
            print("Error al conectar a la base de datos:", e)
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

#SP
# USE [MilPagos]
# GO
# /****** Object:  StoredProcedure [dbo].[SP_consultaHistoricoPago_BGENTE]    Script Date: 3/30/2023 11:16:45 AM ******/
# SET ANSI_NULLS ON
# GO
# SET QUOTED_IDENTIFIER ON
# GO

# -- =============================================
# -- Author:		mggy@sistemasemsys.com
# -- Create date: 17/11/2016
# -- Description:	Consulta la información de un Pago a Comercio
# -- =============================================
# create PROCEDURE [dbo].[SP_consultaHistoricoPago_BGENTE]
# 	@fecha date,
# 	@tipoConsulta int
# AS
# BEGIN		
# 	IF	@tipoConsulta = 1
	
# 		SELECT 
# 		hisId,a.aboCodAfi,a.aboCodComercio,a.aboTerminal,hisLote,hisRecordTDD,hisAmountTDD,hisRecordTDC,hisAmountTDC,
# 		hisAmountTDCImpuesto,hisAmountIVA,hisAmountComisionBanco,hisAmountTotal,hisFechaProceso,hisFechaEjecucion,
# 		hisComisionMantenimiento,hisIvaSobreMantenimiento,hisComisionBancaria,hisNetoComisionBancaria,hisDebitoContraCargo,
# 		a.aboCodAfi,a.aboCodComercio,a.aboTerminal,
# 		--aboCodBanco,
# 		case when (ct.id <> 0 or ct.id <> '0') then ct.cod_banco else aboCodBanco end as aboCodBanco,
# 		--aboNroCuenta,
# 		case when (ct.id <> 0 or ct.id <> '0') then ct.nro_cuenta else aboNroCuenta end as aboNroCuenta,
# 		aboTipoCuenta,aboFreg,aboCod,estatusId,pagoContado,fechaPago,montoEquipoUSD,montoEquipoBs,ivaEquipoBs,
# 		montoTotalEquipoBs,comerCod,comerDesc,comerTipoPer,a.aboCodBanco as comerCodigoBanco,a.aboNroCuenta as comerCuentaBanco,comerPagaIva,
# 		comerCodUsuario,comerCodPadre,
# 		--comerRif,
# 		case when (ct.id <> 0 or ct.id <> '0') then ct.rif else comerRif end as comerRif,
# 		c.comerRif as comerRifCliente,
# 		comerFreg,comerCodTipoCont,comerInicioContrato,comerFinContrato,comerExcluirPago,comerCodCategoria,
# 		comerGarantiaFianza,comerModalidadGarantia,comerMontoGarFian,comerModalidadPos,comerTipoPos,comerRecaudos,
# 		comerDireccion,comerObservaciones,comerCodAliado,comerEstatus,comerHorario,comerImagen,comerPuntoAdicional,comerCodigoBanco2,comerCuentaBanco2,comerCodigoBanco3,
# 		comerCuentaBanco3,comerDireccionHabitacion,comerDireccionPos,comerDiasOperacion,comerFechaGarFian,contCode,
# 		contCodComer,contCodUsuario,contNombres,contApellidos,contTelefLoc,contTelefMov,contMail,contFreg,al.id,aliIdUsuario,
# 		aliTipoIdentificacion,aliIdentificacion,aliApellidos,aliNombres,aliSexo,aliFechaNacimiento,aliCodigoTelHabitacion,
# 		aliTelefonoHabitacion,aliCodigoCelular,aliCelular,aliEmail,aliProfesion,aliDireccion,aliCodZonaAtencion,
# 		aliCodModalidadPago,aliCuentaAbono,aliObservaciones,aliCodEstatus,aliRecaudos,afiCod,afiDesc,afiCodTipoPer,afiFreg,
# 		--afiCodBan,
# 		case when (ct.id <> 0 or ct.id <> '0') then ct.cod_banco else afiCodBan end as afiCodBan,
# 		--afiNroCuenta
# 		case when (ct.id <> 0 or ct.id <> '0') then ct.nro_cuenta else afiNroCuenta end as afiNroCuenta
		
# 		 FROM Historico h 
# 		INNER JOIN Abonos a ON h.aboCodAfi = a.aboCodAfi 
# 		and h.aboCodComercio = a.aboCodComercio 
# 		and h.aboTerminal = a.aboTerminal 
# 		INNER JOIN Comercios c ON h.aboCodComercio = c.comerCod 
# 		LEFT JOIN Contactos cc ON h.aboCodComercio = cc.contCodComer 
# 		LEFT JOIN Aliados al ON al.id = c.comerCodAliado 
# 		INNER JOIN Afiliados af ON h.aboCodAfi = af.afiCod 
# 		LEFT JOIN cta_bank_pot ct ON ct.id = a.ref_bank
# 		WHERE 
# 		convert(date ,h.hisFechaEjecucion) = @fecha 
# 		and a.ref_bank = 1
# 		ORDER BY h.aboCodComercio
		
	
# 	ELSE IF @tipoConsulta = 2
	
# 		SELECT SUM(h.hisAmountTotal) as montoAbonoAliado ,al.id, al.aliTipoIdentificacion, al.aliIdentificacion, al.aliApellidos,
# 			al.aliNombres, al.aliEmail, al.aliDireccion, al.aliCodZonaAtencion, al.aliCodModalidadPago, al.aliCuentaAbono,
# 			al.aliCodEstatus   
# 		FROM Historico h INNER JOIN Comercios c ON h.aboCodComercio = c.comerCod INNER JOIN Abonos a ON h.aboCodAfi = a.aboCodAfi and h.aboCodComercio = a.aboCodComercio and h.aboTerminal = a.aboTerminal LEFT JOIN Contactos cc ON h.aboCodComercio = cc.contCodComer INNER JOIN Aliados al ON al.id = c.comerCodAliado INNER JOIN Afiliados af ON h.aboCodAfi = af.afiCod
# 		WHERE convert(date ,h.hisFechaEjecucion) = @fecha 
# 		GROUP BY al.id, al.aliTipoIdentificacion, al.aliIdentificacion, al.aliApellidos,
# 			al.aliNombres, al.aliEmail, al.aliDireccion, al.aliCodZonaAtencion, al.aliCodModalidadPago, al.aliCuentaAbono,
# 			al.aliCodEstatus	
# END
