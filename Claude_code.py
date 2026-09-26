from google import genai
import os
from dotenv import load_dotenv

load_dotenv(override=True)

client = genai.Client(api_key=os.getenv("api_key"))

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)