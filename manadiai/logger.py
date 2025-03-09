import json
from datetime import datetime
from typing import Optional
from pathlib import Path


class JSONLStorage:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.filepath.parent.mkdir(parents=True, exist_ok=True)

    def save(self, entry: dict):
        with self.filepath.open('a', encoding='utf-8') as f:
            json.dump(entry, f)
            f.write('\n')

    def load_all(self) -> list:
        if not self.filepath.exists():
            return []

        with self.filepath.open('r', encoding='utf-8') as f:
            return [json.loads(line) for line in f]


class GenAILogger:
    def __init__(self, storage_path: str = 'interactions.jsonl'):
        self.storage = JSONLStorage(storage_path)

    def log_interaction(
        self, prompt: str, response: str, feedback: Optional[str] = None
    ):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "prompt": prompt.strip(),
            "response": response.strip(),
            "feedback": feedback.strip() if feedback else None,
        }
        self.storage.save(entry)

    def get_all_interactions(self) -> list:
        return self.storage.load_all()
