# My First AI Agent

A small Python script that talks to Google's Gemini API — my first step toward building an AI agent.

## What it does

`Claude_code.py` sends a prompt to Gemini and prints the response using the `google-genai` SDK.

## Setup

```bash
pip install google-genai python-dotenv
```

Create a `.env` file in the project root (this file is gitignored — never commit it):

```
api_key = 'your-gemini-api-key'
```

Get a free API key at https://aistudio.google.com/apikey

## Run

```bash
python3 Claude_code.py
```

## Notes

- `load_dotenv()` loads the key from `.env` — without it, `os.getenv` only reads shell variables.
- `.env` values are skipped if the same variable already exists in the shell. Use `load_dotenv(override=True)` or `unset` the variable if you see `API_KEY_INVALID` errors.
