import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("where is API key")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-20b"
role="user"
prompt="suggest name for my company"
#message me role and content
message_system={
    "role":"system",
    "content":"you are a brand manager , who suggests name for my clothing company and name should be one word"
}
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages, temperature=2)
#print(response)

print("##########################")

answer=response.choices[0].message.content
print(answer)