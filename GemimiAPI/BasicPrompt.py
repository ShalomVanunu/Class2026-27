import APIKEY
from google import genai

key= APIKEY.KEY

client = genai.Client(api_key=key)

prompt = " explain about electrical car in 2 sentences"
model = "gemini-2.5-flash"

response = client.models.generate_content(model= model, contents=prompt)
print(response.text)



