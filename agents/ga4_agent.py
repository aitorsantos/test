from tools.ga4_tool import get_ga4_data


class GA4Agent:
    """Agent that analyzes GA4 traffic."""

    def ejecutar(self):
        df = get_ga4_data()
        low_visits = df[df['visits'] < 100]
        return {
            'resumen': low_visits.to_dict(orient='records')
        }
