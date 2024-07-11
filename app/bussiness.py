import pandas as pd
from datetime import datetime
from .data_access import DataAccess
from .entities import ExchangeRate

class Bussiness:
    def __init__(self):
        self.client = DataAccess()
        try:
            self.excel_data = self.client.read_excel('data/resultado.xls')
            self.excel_data['Fecha'] = pd.to_datetime(self.excel_data['Fecha'])
        except Exception as e:
            print(f"Error al leer el archivo Excel: {e}")
            self.excel_data = pd.DataFrame(columns=['Fecha', 'Compra', 'Venta'])

    def get_exchange_rate(self, date):
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            row = self.excel_data[self.excel_data['Fecha'] == date_obj]

            if not row.empty:
                compra = row.iloc[0]['Compra']
                venta = row.iloc[0]['Venta']
            else:
                compra_xml, venta_xml = self.client.obtener_tipo_cambio(date)
                compra = float(self.client.procesar_xml(compra_xml))
                venta = float(self.client.procesar_xml(venta_xml))

            return round(compra, 2), round(venta, 2), date_obj.strftime('%Y-%m-%d')
        except Exception as e:
            print(f"Error al obtener el tipo de cambio: {e}")
            raise ValueError("No se pudo obtener el tipo de cambio para la fecha proporcionada.")
