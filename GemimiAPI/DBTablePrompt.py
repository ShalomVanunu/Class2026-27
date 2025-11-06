import APIKEY
from google import genai

key= APIKEY.KEY

client = genai.Client(api_key=key)

prompt = """you are cyber teacher learning SQL langauge. crete example table with 20 random data
the table has the columns : ID, CarName, Mount of Production , Mount of sells.
give me just the table data
table data :
"""
model = "gemini-2.5-flash"

response = client.models.generate_content(model= model, contents=prompt)
print(response.text)



