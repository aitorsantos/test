from datetime import date


def generate_report(results):
    """Return a simple text report summarizing agent results."""
    lines = [f"Reporte diario - {date.today().isoformat()}"]
    for name, result in results.items():
        lines.append(f"## {name}")
        lines.append(str(result))
    return '\n'.join(lines)
