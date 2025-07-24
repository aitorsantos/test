from tools.excel_tool import get_campaign_metrics


class ExcelAgent:
    """Agent that analyzes financial metrics."""

    def ejecutar(self):
        df = get_campaign_metrics()
        high_cpa = df[df['CPA'] > 20.0]
        return {
            'resumen': high_cpa.to_dict(orient='records')
        }
