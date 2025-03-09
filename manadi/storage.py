import json

class JSONLStorage:
    def __init__(self, filepath):
        self.filepath = filepath

    def save(self, entry):
        with open(self.filepath, 'a', encoding='utf-8') as f:
            json.dump(entry, f)
            f.write('\n')

    def load_all(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return [json.loads(line) for line in f]
