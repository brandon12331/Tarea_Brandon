from flask import render_template, request
from .bussiness import Bussiness
from .entities import ExchangeRate

from . import app

business_service = Bussiness()

@app.route('/', methods=['GET', 'POST'])
def index():
    exchange_rate = None
    selected_date = None
    messages = []
    if request.method == 'POST':
        date = request.form['fecha']
        try:
            compra, venta, selected_date = business_service.get_exchange_rate(date)
            exchange_rate = ExchangeRate(compra, venta)
        except ValueError as e:
            messages.append(('error', str(e)))
        except Exception as e:
            messages.append(('error', f'Error inesperado: {str(e)}'))
    return render_template('index.html', exchange_rate=exchange_rate, selected_date=selected_date, messages=messages)
