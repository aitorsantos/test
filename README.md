# Proyecto CrewAI

Este proyecto simula un conjunto de agentes que analizan datos de campañas publicitarias y generan un reporte diario.

## Estructura
- `agents/` agentes individuales para Ads, Excel y GA4.
- `tools/` utilidades que simulan obtención de datos.
- `memory/` almacenamiento de memoria en JSON.
- `feedback/` registro de feedback manual.
- `reporting/` generación de reporte diario.
- `ui/` interfaz mínima en Streamlit.

## Uso
1. Instalar dependencias `pip install -r requirements.txt`.
2. Ejecutar `python run_agent.py` para lanzar el ciclo diario.
3. Opcionalmente ejecutar `streamlit run ui/streamlit_app.py` para introducir feedback.

También se puede usar `docker-compose up` para ejecutar en contenedor.
