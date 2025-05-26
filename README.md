
# 🤖 Mental Health Chatbot for War-Affected Communities

A bilingual (Arabic–English) chatbot that helps users recognize symptoms of common mental health disorders like **depression**, **anxiety**, and **PTSD**, and provides compassionate, informative advice — especially tailored for people in or displaced from war zones.

---

## 🧠 Features

- 🔍 **Keyword-Based Detection** using NLTK
- 🧾 **Mental Health Advice** based on condition
- 🌐 **Language Support**: Arabic & English
- 💬 **Two Modes**:
  - `Rule-based`: Lightweight, offline logic
  - `GPT-powered`: More natural, AI-generated support via OpenAI

---

## 💡 Example Prompts

- "I feel worthless and tired all the time."
- "أعاني من كوابيس وذكريات مؤلمة كل ليلة"
- "I can't stop panicking and my heart races fast."

---

## 🛠️ How to Run It

### 1. 🔧 Installation

```bash
pip install openai nltk
````




### ▶️ Run the Chatbot

```bash
python wzmh.py
```

When prompted:

* Enter `1` for rule-based replies (fast, offline)
* Enter `2` for GPT-generated replies (more natural, needs internet & OpenAI API)

---

## 🗣️ Language Detection

The chatbot auto-detects whether the user is typing in **Arabic or English**, and responds in the same language.

---

## 🧰 Technologies Used

| Tool     | Purpose                               |
| -------- | ------------------------------------- |
| `nltk`   | Tokenization and keyword matching     |
| `openai` | GPT-3.5 conversational support        |
| `re`     | Language detection and input cleaning |

---

## 🤲 Ethical Considerations

This chatbot is **not a substitute for professional mental health care**. It's meant to offer **comfort**, **guidance**, and **early detection support** — especially in communities affected by conflict and crisis.

---


---

## 🙌 Acknowledgments

* Inspired by the emotional needs of war-affected populations.
* Built with compassion, language inclusivity, and accessibility in mind.

---

## 📬 Feedback

We welcome contributions and improvements. If you have ideas for extending trauma categories, improving language support, or deploying this on platforms like **Telegram**, feel free to open an issue or PR.

---

```


