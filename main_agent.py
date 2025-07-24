from agents.ads_agent import AdsAgent
from agents.excel_agent import ExcelAgent
from agents.ga4_agent import GA4Agent
from feedback.feedback_store import load_feedback
from memory.memory_manager import save_memory
from reporting.daily_report import generate_report


def ciclo_diario():
    results = {}

    ads_agent = AdsAgent()
    results['ads'] = ads_agent.ejecutar()

    excel_agent = ExcelAgent()
    results['excel'] = excel_agent.ejecutar()

    ga4_agent = GA4Agent()
    results['ga4'] = ga4_agent.ejecutar()

    feedback = load_feedback()
    save_memory({'results': results, 'feedback': feedback})

    report = generate_report(results)
    print(report)
    return report
