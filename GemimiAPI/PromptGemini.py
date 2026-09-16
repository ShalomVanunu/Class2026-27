from dotenv import load_dotenv
from google import genai

load_dotenv() #load the API key from .env

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)

