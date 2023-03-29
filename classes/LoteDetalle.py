class LoteDetalle:
    
    def __init__(self):
        self.id = None
        self.lotCodCompania = None
        self.lotNumLote = None
        self.lotTipoRegistro = 0
        self.lotCodMonedaDeb = None
        self.lotCodMonedaCred = None
        self.lotActividadEcom: int = 0
        self.lotMotivoOpe: int = 0
        self.lotCuentaDebito = None
        self.lotFechaValor = None
        self.lotMontoTotal = None
        self.lotCantidadPagos = 0
        self.lotNumPagoProveedor = None
        self.lotNumFactura = None
        self.lotEmailBeneficiario = None
        self.lotRifBeneficiario = None
        self.lotNombreBeneficiario = None
        self.lotMonto: int = 0.0
        self.lotTipoPago: int = 0
        self.lotCodOficBanco: int = 0
        self.lotCuentaBeneficiario = None
        self.lotConceptoPago = None
        self.lotCodBancoBenef = None
        self.lotTipoCodBanco = None
        self.lotNombreBancoBenef = None
        self.lotDireccionBancoBenef = None

    def init__line1(lotCodCompania: str, nombre_archivo: str, hisId: str, lotTipoRegistro: str, contMail: str, comerRif:str, hisAmountTotal: str):
        lote = LoteDetalle()
        lote.lotCodCompania =lotCodCompania
        lote.lotNumLote = nombre_archivo
        lote.lotNumPagoProveedor = hisId
        lote.lotTipoRegistro = lotTipoRegistro
        lote.lotEmailBeneficiario= contMail
        lote.lotRifBeneficiario = comerRif
        lote.lotMontoTotal = hisAmountTotal
        return lote

    def init__line2(lotCodCompania: str, nombre_archivo: str, hisId: str, lotTipoRegistro: str, hisAmountTotal: str, comerDesc: str, tipoCuentaAbono: str, aboNroCuenta: str,
            lotCodMonedaCred: str, lotCodMonedaDeb: str, lotConceptoPago: str,lotCodBancoBenef: str, lotTipoCodBanco: str, lotMotivoOpe: str,lotActividadEcom: str, lotCuentaDebito: str):
        lote = LoteDetalle()
        lote.lotCodCompania =lotCodCompania
        lote.lotNumLote = nombre_archivo
        lote.lotNumPagoProveedor = hisId
        lote.lotTipoRegistro = lotTipoRegistro
        lote.lotMontoTotal = hisAmountTotal
        lote.lotNombreBeneficiario = comerDesc
        lote.lotTipoPago = tipoCuentaAbono
        lote.lotCuentaBeneficiario = aboNroCuenta
        lote.lotCodMonedaCred = lotCodMonedaCred
        lote.lotCodMonedaDeb = lotCodMonedaDeb
        lote.lotConceptoPago = lotConceptoPago
        lote.lotCodBancoBenef = lotCodBancoBenef
        lote.lotTipoCodBanco =lotTipoCodBanco
        lote.lotMotivoOpe = lotMotivoOpe
        lote.lotActividadEcom = lotActividadEcom
        lote.lotCuentaDebito = lotCuentaDebito
        return lote

    def __str__(self):
        return f"LotDetalle(id={self.id}, lotCodCompania={self.lotCodCompania}, lotNumLote={self.lotNumLote}, " \
               f"lotTipoRegistro={self.lotTipoRegistro}, lotCodMonedaDeb={self.lotCodMonedaDeb}, " \
               f"lotCodMonedaCred={self.lotCodMonedaCred}, lotActividadEcom={self.lotActividadEcom}, " \
               f"lotMotivoOpe={self.lotMotivoOpe}, lotCuentaDebito={self.lotCuentaDebito}, " \
               f"lotFechaValor={self.lotFechaValor}, lotMontoTotal={self.lotMontoTotal}, " \
               f"lotCantidadPagos={self.lotCantidadPagos}, lotNumPagoProveedor={self.lotNumPagoProveedor}, " \
               f"lotNumFactura={self.lotNumFactura}, lotEmailBeneficiario={self.lotEmailBeneficiario}, " \
               f"lotRifBeneficiario={self.lotRifBeneficiario}, lotNombreBeneficiario={self.lotNombreBeneficiario}, " \
               f"lotMonto={self.lotMonto}, lotTipoPago={self.lotTipoPago}, lotCodOficBanco={self.lotCodOficBanco}, " \
               f"lotCuentaBeneficiario={self.lotCuentaBeneficiario}, lotConceptoPago={self.lotConceptoPago}, " \
               f"lotCodBancoBenef={self.lotCodBancoBenef}, lotTipoCodBanco={self.lotTipoCodBanco}, " \
               f"lotNombreBancoBenef={self.lotNombreBancoBenef}, lotDireccionBancoBenef={self.lotDireccionBancoBenef})"

