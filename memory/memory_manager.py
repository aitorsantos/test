import json
from pathlib import Path


MEMORY_FILE = Path('memory.json')


def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_memory(entry):
    data = load_memory()
    data.append(entry)
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
