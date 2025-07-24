import pandas as pd


def get_ga4_data():
    """Return simulated GA4 traffic and events."""
    data = pd.DataFrame({
        'page': ['/', '/about', '/purchase'],
        'visits': [1000, 300, 50],
        'events': [200, 50, 45],
    })
    return data
