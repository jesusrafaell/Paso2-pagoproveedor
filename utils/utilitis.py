import datetime
from typing import List, Tuple, Union
from classes.Historico import Historico
import re

class Util:
    @staticmethod
    def delete_sings(cadena):
        # Definir el patrón de caracteres especiales
        patron = r'[^a-zA-Z0-9\s]'
        
        # Eliminar los caracteres especiales utilizando expresiones regulares
        cadena_sin_especiales = re.sub(patron, '', cadena)
    
        return cadena_sin_especiales

    def rounder (num: float):
        if num.is_integer():
            return  str(int(num)) + '.00'
        else:
            return "{:.2f}".format(num)
        
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
    
    def get_dataBanco(historicos: List[Historico]) -> Tuple[str, str]:
        comerRif = ""
        nro_cuenta = ""

        for h in historicos:
            if not comerRif:
                comerRif = h.comerRifBanco
            elif h.comerRifBanco != comerRif:
                print('Más de un comerRif encontrado')
                raise ValueError('Más de un comerRif encontrado')
            
            if not nro_cuenta:
                nro_cuenta = h.aboNroCuentaBanco
            elif h.aboNroCuentaBanco != nro_cuenta:
                print('Más de un comerRif encontrado')
                raise ValueError('Más de un número de cuenta encontrado')

        if not comerRif or not nro_cuenta:
            print('Más de un comerRif encontrado')
            raise ValueError('No se encontró ningún historial')
        
        return comerRif, nro_cuenta

    def get_rif_prefix(rif_prefix) -> str: 
        tipoDoc = "01"
        if rif_prefix == "V":
            tipoDoc = "01"
        elif rif_prefix == "P":
            tipoDoc = "02"
        elif rif_prefix == "J":
            tipoDoc = "04"
        elif rif_prefix == "E":
            tipoDoc = "08"
        return tipoDoc

    def getTipoCuentaAbono(value: str) -> str: 
        if value == "0104":
            return "1"
        else:
            return "3"

    def convierteFechaSql(fecha: str) -> Union[None, datetime.date]:
        # print(fecha)
        try:
            fechaUtil = datetime.strptime(fecha, '%d-%m-%Y')
        except ValueError:
            return None

        fechaSql = fechaUtil.date()

        return fechaSql

    def rightPad(string: str, length: int, fill_char: str):
        if len(string) > length:
            return string[:length]
        else:
            return string + (fill_char * (length - len(string)))

    def leftPad(string: str, longitud: int, caracter: str):
        # Convierte el número a una cadena de texto y rellena con el carácter especificado
        cadena_rellena = str(string).rjust(longitud, caracter)
        
        # Si la cadena resultante es más larga que la longitud especificada, cártala
        if len(cadena_rellena) > longitud:
            cadena_rellena = cadena_rellena[:longitud]
            
        return cadena_rellena