import json
from pathlib import Path


FEEDBACK_FILE = Path('feedback_store.json')


def load_feedback():
    if FEEDBACK_FILE.exists():
        with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_feedback(entry):
    data = load_feedback()
    data.append(entry)
    with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
