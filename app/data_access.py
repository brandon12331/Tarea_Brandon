from zeep import Client
from zeep.transports import Transport
from datetime import datetime
import xml.etree.ElementTree as ET
import pandas as pd

class DataAccess:
    def __init__(self):
        wsdl_url = 'https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx?WSDL'
        self.client = Client(wsdl=wsdl_url, transport=Transport(timeout=10))

    def obtener_tipo_cambio(self, fecha):
        if isinstance(fecha, str):
            # Convertir la cadena a datetime
            fecha = datetime.strptime(fecha, '%Y-%m-%d')
        elif not isinstance(fecha, datetime):
            raise ValueError("La fecha debe ser una cadena en formato 'YYYY-MM-DD' o un objeto datetime")
        fecha_str = fecha.strftime('%d/%m/%Y')

        parametros_compra = {
            'Indicador': 317,  # Código del indicador para tipo de cambio compra
            'FechaInicio': fecha_str,
            'FechaFinal': fecha_str,
            'Nombre': 'Brandon',
            'SubNiveles': 'N',
            'CorreoElectronico': 'brandonandino91@gmail.com',
            'Token': 'PNRMRDOAL2'
        }
        parametros_venta = {
            'Indicador': 318,  # Código del indicador para tipo de cambio venta
            'FechaInicio': fecha_str,
            'FechaFinal': fecha_str,
            'Nombre': 'Brandon',
            'SubNiveles': 'N',
            'CorreoElectronico': 'brandonandino91@gmail.com',
            'Token': 'PNRMRDOAL2'
        }

        try:
            compra = self.client.service.ObtenerIndicadoresEconomicosXML(**parametros_compra)
            venta = self.client.service.ObtenerIndicadoresEconomicosXML(**parametros_venta)
        except Exception as e:
            print(f"Error al obtener tipo de cambio para la fecha {fecha_str}: {e}")
            return None, None

        return compra, venta

    def procesar_xml(self, xml_response):
        try:
            # Parsear el XML recibido
            root = ET.fromstring(xml_response)
            # Encuentra el tag que contiene el tipo de cambio
            tipo_cambio_tag = root.find('.//NUM_VALOR')

            if tipo_cambio_tag is not None:
                tipo_cambio = tipo_cambio_tag.text
                return tipo_cambio
            else:
                return "No se encontró el tipo de cambio, posiblemente ingresó una fecha no registrada o una fecha que está fuera de rango"
        except ET.ParseError as parse_error:
            return f"Error de parsing XML: {parse_error} en el XML recibido: {xml_response[:100]}"  # Mostrar los primeros 100 caracteres del XML
        except Exception as e:
            return f"Error al procesar respuesta XML: {e} el XML recibido : {xml_response}"

    def read_excel(self, file_path):
        df = pd.read_excel(file_path)
        return df
