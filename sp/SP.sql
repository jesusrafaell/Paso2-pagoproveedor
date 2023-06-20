ALTER PROCEDURE [dbo].[SP_consultaHistoricoPago_BGENTE]
	@fecha date,
	@tipoConsulta int
AS
BEGIN		
	IF	@tipoConsulta = 1
		SELECT 
		hisId,
    a.aboCodAfi,
    a.aboCodComercio,
    a.aboTerminal,
    hisLote,
    hisRecordTDD,
    hisRecordTDC,
    hisAmountTDD,
    hisAmountTDC,
    hisAmountTDCImpuesto,
    hisAmountIVA,
    hisAmountComisionBanco,
    hisAmountTotal,
    hisFechaEjecucion,
    hisFechaProceso,
    comerCodigoBanco,
    comerCuentaBanco,
    ct.rif as comerRifBanco,
		case when (ct.id <> 0 or ct.id <> '0') then ct.nro_cuenta else aboNroCuenta end as aboNroCuenta,
		a.aboNroCuenta as comerCuentaBanco,
    aboTipoCuenta,
    comerDesc,
    comerTipoPer,
    comerPagaIva,
    comerCodUsuario,
		c.comerRif as comerRifCliente,
		case when (ct.id <> 0 or ct.id <> '0') then ct.rif else comerRif end as comerRif,
    cc.contNombres as contNombre, contNombres,cc.contApellidos as contApellidos,
    contTelefLoc,
    contTelefMov,
    contMail,
    afiDesc,
    afiCodTipoPer,
    comerCodPadre
		FROM Historico h 
      INNER JOIN Abonos a ON h.aboCodAfi = a.aboCodAfi 
      and h.aboCodComercio = a.aboCodComercio 
      and h.aboTerminal = a.aboTerminal 
      INNER JOIN Comercios c ON h.aboCodComercio = c.comerCod 
      LEFT JOIN Contactos cc ON h.aboCodComercio = cc.contCodComer 
      LEFT JOIN Aliados al ON al.id = c.comerCodAliado 
      INNER JOIN Afiliados af ON h.aboCodAfi = af.afiCod 
      LEFT JOIN cta_bank_pot ct ON ct.id = a.ref_bank
		WHERE 
      convert(date ,h.hisFechaEjecucion) = @fecha 
      and hisAmountTotal > 0
      and a.ref_bank = 1
		ORDER BY h.aboCodComercio
		
	ELSE IF @tipoConsulta = 2
	
		SELECT SUM(h.hisAmountTotal) as montoAbonoAliado ,al.id, al.aliTipoIdentificacion, al.aliIdentificacion, al.aliApellidos,
			al.aliNombres, al.aliEmail, al.aliDireccion, al.aliCodZonaAtencion, al.aliCodModalidadPago, al.aliCuentaAbono,
			al.aliCodEstatus   
		FROM Historico h INNER JOIN Comercios c ON h.aboCodComercio = c.comerCod INNER JOIN Abonos a ON h.aboCodAfi = a.aboCodAfi and h.aboCodComercio = a.aboCodComercio and h.aboTerminal = a.aboTerminal LEFT JOIN Contactos cc ON h.aboCodComercio = cc.contCodComer INNER JOIN Aliados al ON al.id = c.comerCodAliado INNER JOIN Afiliados af ON h.aboCodAfi = af.afiCod
		WHERE convert(date ,h.hisFechaEjecucion) = @fecha 
		GROUP BY al.id, al.aliTipoIdentificacion, al.aliIdentificacion, al.aliApellidos,
			al.aliNombres, al.aliEmail, al.aliDireccion, al.aliCodZonaAtencion, al.aliCodModalidadPago, al.aliCuentaAbono,
			al.aliCodEstatus	

	ELSE IF @tipoConsulta = 3
		SELECT 
		hisId,
    a.aboCodAfi,
    a.aboCodComercio,
    a.aboTerminal,
    hisLote,
    hisRecordTDD,
    hisRecordTDC,
    hisAmountTDD,
    hisAmountTDC,
    hisAmountTDCImpuesto,
    hisAmountIVA,
    hisAmountComisionBanco,
    hisAmountTotal,
    hisFechaEjecucion,
    hisFechaProceso,
    comerCodigoBanco,
    comerCuentaBanco,
    ct.rif as comerRifBanco,
		case when (ct.id <> 0 or ct.id <> '0') then ct.nro_cuenta else aboNroCuenta end as aboNroCuenta,
		a.aboNroCuenta as comerCuentaBanco,
    aboTipoCuenta,
    comerDesc,
    comerTipoPer,
    comerPagaIva,
    comerCodUsuario,
		c.comerRif as comerRifCliente,
		case when (ct.id <> 0 or ct.id <> '0') then ct.rif else comerRif end as comerRif,
    cc.contNombres as contNombre, contNombres,cc.contApellidos as contApellidos,
    contTelefLoc,
    contTelefMov,
    contMail,
    afiDesc,
    afiCodTipoPer,
    comerCodPadre
		FROM Historico_pago_proveedores h 
      INNER JOIN Abonos a ON h.aboCodAfi = a.aboCodAfi 
      and h.aboCodComercio = a.aboCodComercio 
      and h.aboTerminal = a.aboTerminal 
      INNER JOIN Comercios c ON h.aboCodComercio = c.comerCod 
      LEFT JOIN Contactos cc ON h.aboCodComercio = cc.contCodComer 
      LEFT JOIN Aliados al ON al.id = c.comerCodAliado 
      INNER JOIN Afiliados af ON h.aboCodAfi = af.afiCod 
      LEFT JOIN cta_bank_pot ct ON ct.id = a.ref_bank
		WHERE 
      hisAmountTotal > 0 and a.ref_bank = 1
		ORDER BY h.aboCodComercio
		
END