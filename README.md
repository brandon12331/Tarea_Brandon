# Proyecto de Consulta de Tipo de Cambio 
# Estudiante: Brandon Andino López

¡Bienvenido! Este es un proyecto simple para consultar el tipo de cambio de compra y venta de una moneda en una fecha específica. Utilizamos Flask para el backend, Zeep para consumir un servicio web, y Pandas para manejar los datos.

## Requisitos

- Python 3.x
- Flask
- Pandas
- Zeep

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/brandon12331/Tarea_brandon.git
    cd Tarea_brandon
    ```

2. (Opcional) Crea y activa un entorno virtual para mantener las dependencias organizadas:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

4. Asegúrate de que el archivo Excel `resultado.xls` está en la carpeta `data` en la raíz del proyecto.

## Cómo Ejecutar

1. Asegúrate de estar en el entorno virtual si estás usando uno.
2. Ejecuta la aplicación:

    ```bash
    python run.py
    ```

3. Abre tu navegador y ve a `http://127.0.0.1:5000/`.

## Estructura del Proyecto

- **`app/__init__.py`**: Configuración de la aplicación Flask.
- **`app/routes.py`**: Define las rutas y la lógica principal.
- **`app/bussiness.py`**: Maneja la lógica de negocio para obtener los tipos de cambio.
- **`app/data_access.py`**: Se comunica con el servicio web y maneja el acceso a datos.
- **`app/entities.py`**: Define la entidad `ExchangeRate`.
- **`static/styles.css`**: Estilos CSS para la página web.
- **`templates/index.html`**: Plantilla HTML principal.
- **`data/resultado.xls`**: Archivo Excel con los datos de los tipos de cambio.
- **`run.py`**: Script para iniciar la aplicación.

## Uso

1. Ve a `http://127.0.0.1:5000/` en tu navegador.
2. Selecciona una fecha y haz clic en "Consultar".
3. Verás el tipo de cambio de compra y venta para la fecha seleccionada.

## Solución de Problemas

- **Problemas con dependencias**: Asegúrate de instalar todo correctamente con `pip install -r requirements.txt`.
- **Archivo Excel no encontrado**: Verifica que `resultado.xls` está en la carpeta `data`.


Autor: Brandon Antonio Andino López
