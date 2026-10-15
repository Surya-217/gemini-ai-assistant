# Gemini AI Assistant

A command-line AI assistant built with Python and Google's Gemini API.

## Features

- AI-powered responses using Gemini
- Conversation memory during a session
- `/help` - Show available commands
- `/clear` - Start a fresh conversation
- `/exit` - Quit the assistant
- Retry configuration for temporary API errors

## Requirements

- Python 3.10+
- A Gemini API key from Google AI Studio

## Setup

### 1. Create and activate a virtual environment

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -U google-genai
```

### 3. Set your API key

```powershell
$env:GEMINI_API_KEY = Read-Host "Enter your Gemini API key"
```

### 4. Run the assistant

```powershell
python main.py
```

## Security

Never commit API keys or `.env` files to GitHub.

## Built With

- Python
- Google Gen AI SDK
- Gemini API
