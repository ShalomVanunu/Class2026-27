import APIKEY
from google import genai

key= APIKEY.KEY

client = genai.Client(api_key=key)

def response_prompt(prompt):
    model = "gemini-2.0-flash"
    response = client.models.generate_content(model= model, contents=prompt)
    return  response.text

context = ""
while True:
    user_prompt = input(" Enter prompt [bye to exit] :")
    if user_prompt.lower() == "bye":
        break
    prompt = f"""context :  {context} \n
    {user_prompt}
    result :"""
    context += response_prompt(prompt)+"\n"
    print(context)



