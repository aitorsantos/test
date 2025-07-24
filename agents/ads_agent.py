from tools.ads_tool import get_ads_data


class AdsAgent:
    """Agent that analyzes ad performance."""

    def ejecutar(self):
        data = get_ads_data()
        low_ctr = [kw for kw, ctr in data.items() if ctr < 0.02]
        return {
            'resumen': f'Keywords con bajo CTR: {", ".join(low_ctr)}'
        }
