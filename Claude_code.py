from google import genai
import os
from dotenv import load_dotenv

load_dotenv(override=True)

client = genai.Client(api_key=os.getenv("api_key"))

user_probmt = input('Enter your prompt: ')
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input=user_probmt
)
print(interaction.output_text)