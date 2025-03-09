# 🚀 manadiai: take your genai data with you

**Capture, organize, and fine-tune from your GenAI interactions effortlessly.**

---

## 📚 Overview

**manadiair** automatically captures and preserves your interactions with Generative AI models—including your prompts, AI responses, and feedback—in structured formats suitable for fine-tuning your own personalized GenAI models.

---

## ✨ Features

- **Seamless Interaction Logging:** Automatically records your prompts, responses from GenAI bots, and your optional feedback.
- **Structured Data Storage:** Saves interactions in a JSONL file, ready-to-use for fine-tuning.
- **Middleware and Browser Integration:** Supports capturing interactions via API middleware or browser extensions.
- **Flexible Export:** Export your logged data in formats supported by major fine-tuning platforms (OpenAI, HuggingFace).

---

## 📖 How It Works

- **Prompt & Response Capture:** Every interaction is captured and tagged.
- **Optional Feedback:** Add corrections or feedback directly after each generation.
- **Automatic Structuring:** Captures are structured in JSONL format, ensuring compatibility with standard fine-tuning tools.

Example structured data entry:
```json
{
  "prompt": "What is consistent hashing?",
  "response": "Consistent hashing is a method used in distributed systems...",
  "feedback": "Great explanation, but please simplify further."
}
```

---

## 🛠️ Tech Stack

- **Backend:** Python (FastAPI)
- **Frontend (optional):** Streamlit, React, Chrome Extension
- **Storage:** SQLite / PostgreSQL / JSONL files

---

## 📦 Installation & Setup

Clone the repository:
```bash
git clone https://github.com/matmulai/manadiai.git
cd manadiai
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Start the server:
```bash
uvicorn main:app --reload
```

---

## 🛠️ Usage

- **Interact normally with your GenAI bots through the provided interface.**
- **Your interactions are automatically logged.**
- Export captured data when you're ready for fine-tuning.

---

## 🎯 Fine-tuning Your GenAI Model

- Use the generated `interactions.jsonl` file with platforms like:
  - OpenAI Fine-tuning API
  - HuggingFace Trainer

Example fine-tuning command:
```bash
openai api fine_tunes.create -t interactions.jsonl
```

---

## 🤝 Contributing

We welcome contributions!

- Fork this repository
- Create your branch (`git checkout -b feature/my-feature`)
- Commit your changes (`git commit -m 'Add my feature'`)
- Push your changes (`git push origin feature/my-feature`)
- Create a pull request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

