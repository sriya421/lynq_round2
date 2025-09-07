import os
from dotenv import load_dotenv
from google import genai 
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    print("api key found")
else:
    print("api key not working")

# Initialize the client
client = genai.Client(api_key=api_key)


# Send a simple prompt
user_prompt = input("Enter prompt:")

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=user_prompt
)

print(response.text)





