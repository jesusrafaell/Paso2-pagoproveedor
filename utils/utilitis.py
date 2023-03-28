import datetime

class Utilidades:
        
    @staticmethod
    def convierteFechaSql(fecha):
        df = datetime.datetime.strptime(fecha, '%d-%m-%Y')
        fechaSql = df.date()
        return fechaSql
        
    @staticmethod
    def getFechaActual():
        ahora = datetime.datetime.now()
        formateador = ahora.strftime('%d-%m-%Y')
        return formateador
    
    @staticmethod
    def getFechaActualSql():
        ahora = datetime.datetime.now()
        fechaSql = ahora.date()
        return fechaSql
    
    @staticmethod
    def getHoraActual():
        ahora = datetime.datetime.now()
        formateador = ahora.strftime('%H:%M:%S')
        return formateador
    
    @staticmethod
    def sumarFechasDias(fecha, dias):
        fecha = fecha + datetime.timedelta(days=dias)
        return fecha
    
    @staticmethod
    def restarFechasDias(fecha, dias):
        fecha = fecha - datetime.timedelta(days=dias)
        return fecha
    
    @staticmethod
    def diferenciasDeFechas(fechaInicial, fechaFinal):
        fechaInicial = datetime.datetime.strptime(str(fechaInicial), '%Y-%m-%d')
        fechaFinal = datetime.datetime.strptime(str(fechaFinal), '%Y-%m-%d')
        diferencia = fechaFinal - fechaInicial
        dias = diferencia.days
        return dias
    
    @staticmethod
    def deStringToDate(fecha):
        fechaEnviar = datetime.datetime.strptime(fecha, '%d-%m-%Y')
        return fechaEnviar.date()