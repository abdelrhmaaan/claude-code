from google import genai
import os
from dotenv import load_dotenv

load_dotenv(override=True)

client = genai.Client(api_key=os.getenv("api_key"))

# create a memory for our app

history = []

while True:
    user_probmt = input('Enter your prompt: ')
    if user_probmt.lower() in ['exit', 'quit', 'q']:
        break
    history.append({"role": "user", "parts": [{"text": user_probmt}]})
    interaction = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=history
    )
    print(interaction.text)
    history.append({"role": "model", "parts": [{"text": interaction.text}]})