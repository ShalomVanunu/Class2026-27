import APIKEY
from google import genai

key= APIKEY.KEY

client = genai.Client(api_key=key)

def response_prompt(prompt):
    model = "gemini-2.0-flash"
    response = client.models.generate_content(model= model, contents=prompt)
    return  response.text

while True:
    prompt = input(" Enter prompt [bye to exit] :")
    if prompt.lower() == "bye":
        break
    print(response_prompt(prompt))



