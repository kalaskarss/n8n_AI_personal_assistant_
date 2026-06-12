# 🤖 Personal Assistant Workflow

This project is an **AI-powered personal assistant** built using **n8n (backend automation)** and a **Streamlit app (frontend UI)**.

The assistant can understand user requests, decide what action is needed, use the right tool, and return results — just like a smart executive assistant.

---

## ✨ Features

* 🔎 Answer questions using web search
* 📅 Manage calendar events
* 📧 Read and send emails
* 📝 Create and manage notes
* ✅ Manage tasks (create, view, delete)
* 💰 Track expenses
* 🧠 Conversational memory for follow-up queries

---

## 📋 Prerequisites

Before you start, ensure you have:

- **Python 3.12+** installed
- **n8n** running locally (http://localhost:5678)
- **pip** or **uv** package manager
- Google Cloud credentials (for Google API access)

---

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/kalaskarss/n8n_AI_personal_assistant_.git
cd n8n_AI_personal_assistant_
```

2. **Create a virtual environment**
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
# or if using uv
uv sync
```

---

## ⚙️ Configuration

1. **Create a `.env` file** in the project root:
```bash
cp .env.example .env
```

2. **Add your n8n webhook URL**:
```
N8N_WEBHOOK_URL=http://localhost:5678/webhook/YOUR_WEBHOOK_ID
N8N_WEBHOOK_TEST_URL=http://localhost:5678/webhook-test/YOUR_WEBHOOK_ID
```

3. **Set up n8n**:
   - Configure Google OAuth credentials in n8n
   - Create your workflow and get the webhook URL
   - Update `.env` with the webhook URL

---

## 🏃 Running the App

1. **Start n8n** (if not already running):
```bash
# n8n should be running on http://localhost:5678
```

2. **Run the Streamlit app**:
```bash
streamlit run app.py
```

3. The app will open at `http://localhost:8501`

---

## 🧪 Testing

To test the webhook connection:
```bash
python test_webhook.py
```

---

## 📁 Project Structure

```
n8n_AI_personal_assistant_/
│
├── app.py                    # Main Streamlit app
├── test_webhook.py           # Webhook testing script
├── main.py                   # Entry point
├── sysprompt.md              # System prompt for AI agent
├── .env                      # Environment variables (not in repo)
├── .env.example              # Template for .env file
├── .gitignore               # Git ignore rules
├── pyproject.toml           # Project dependencies
└── README.md                # This file
```

---

## 📚 How It Works (Simple Flow)



## Core Components

### 🤖 AI Agent

The brain of the system.

* Understands user intent
* Decides which tool to use
* Keeps responses short and accurate

### 🧠 Memory

* Remembers recent conversation
* Helps in handling follow-up queries

### 🧰 Tools Connected

The agent can use multiple tools:

* Google Search → for external information
* Google Calendar → manage events
* Gmail → read/send emails
* Google Sheets → track expenses
* Google Docs → manage notes
* Google Tasks → manage to-do items

---

## Example Use Cases

**1. Tasks**
"Show my tasks" → AI fetches tasks and returns list

**2. Calendar**
"Schedule a meeting tomorrow" → Event is created

**3. Email**
"Send an email to HR" → Email is drafted and sent

**4. Expenses**
"Add ₹500 for food" → Expense is saved in sheet

**5. Notes**
"Save this note" → Content is stored in Docs

---

## Streamlit Integration

The Streamlit app is the user interface:

* Takes user input
* Sends it to n8n
* Displays assistant responses


## Summary

This🌐 Streamlit Integration

The Streamlit app is the user interface:

* Takes user input
* Sends it to the n8n webhook
* Displays assistant responses in real-time
* Maintains conversation history

---

## 🔧 Troubleshooting

**Error: "Connection refused" to localhost:5678**
- Make sure n8n is running on your machine
- Check n8n is accessible at http://localhost:5678

**Error: "dotenv not found"**
- Install it: `pip install python-dotenv`

**Error: "N8N_WEBHOOK_URL not set"**
- Create/update `.env` file with your webhook URL
- Ensure the file is in the project root

---

## 📦 Dependencies

All dependencies are listed in `pyproject.toml`:
- `streamlit>=1.53.0` - UI framework
- `requests>=2.31.0` - HTTP requests
- `python-dotenv>=1.0.0` - Environment variable management

---

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!


**Built with ❤️ using n8n + Streamlit + AI**
