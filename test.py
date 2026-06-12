import os
from groq import Groq

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ]
)

print(response.choices[0].message.content)