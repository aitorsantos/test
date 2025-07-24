import pandas as pd


def get_campaign_metrics():
    """Return simulated CPA and ROAS per campaign."""
    data = pd.DataFrame({
        'campaign': ['A', 'B', 'C'],
        'CPA': [10.0, 25.0, 15.0],
        'ROAS': [2.5, 1.2, 3.0],
    })
    return data
