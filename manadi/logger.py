import json
from pathlib import Path
from typing import Optional, List, Dict
import openai

class GenAILogger:
    def __init__(self, storage_path: str = 'interactions.jsonl'):
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

    def log_interaction(self, prompt: str, response: str, feedback: Optional[str] = None) -> None:
        """
        Logs an interaction consisting of a prompt, the GenAI response, and optional feedback.
        """
        entry = {
            "prompt": prompt.strip(),
            "response": response.strip(),
            "feedback": feedback.strip() if feedback else None
        }
        with self.storage_path.open("a", encoding="utf-8") as f:
            json.dump(entry, f)
            f.write('\n')

    def get_all_interactions(self) -> List[Dict]:
        """
        Retrieves all logged interactions from the storage file.
        """
        if not self.storage_exists():
            return []
        with self.storage_path.open('r', encoding="utf-8") as f:
            return [json.loads(line) for line in f]

    def storage_exists(self) -> bool:
        """
        Checks if the storage file exists.
        """
        return self.storage_path.exists()

    def __init__(self, storage_path: str = "interactions.jsonl"):
        """
        Initializes the logger with a path to store interactions.
        """
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

    def fine_tune_openai(self, api_key: str, model: str = "gpt-3.5-turbo") -> Dict:
        """
        Initiates a fine-tuning job with OpenAI using the logged interactions.
        Returns the fine-tuning job response from OpenAI.
        """
        openai.api_key = api_key
        interactions = self.get_all_interactions()

        fine_tune_data = [
            {
                "messages": [
                    {"role": "user", "content": entry["prompt"]},
                    {"role": "assistant", "content": entry["response"]}
                ]
            }
            for entry in interactions if entry["response"]
        ]

        training_file_path = self.storage_path.parent / 'training_data.jsonl'

        with training_file.open('w', encoding="utf-8") as f:
            for item in fine_tune_data:
                json.dump(item, f)
                f.write('\n')

        with training_file.open('rb') as training_file:
            training_response = openai.File.create(file=training_file, purpose='fine-tune')

        fine_tune_response = openai.FineTuningJob.create(
            training_file=training_response.id,
            model=model
        )

        return fine_tune_response