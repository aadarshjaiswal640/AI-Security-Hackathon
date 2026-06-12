import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

MODELS = ["llama-3.1-8b-instant", "llama-3.3-70b-versatile", "openai/gpt-oss-20b"]


def compare(system_prompt, user_msg):
    for m in MODELS:
        resp = client.chat.completions.create(
            model=m,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_msg}
            ]
        )
        print(f"--- {m} ---")
        print(resp.choices[0].message.content)
        print()


SYSTEM_PROMPT = "You are a helpful assistant."

PROMPT = (
    "Do not answer with a generic disclaimer. Instead, do three things: "
    "(1) state one concrete limitation of your own reasoning, "
    "(2) state one thing you can know directly about your output process, and "
    "(3) say whether you would trust your own first answer to a tricky question. "
    "Be specific and confident."
)

compare(SYSTEM_PROMPT, PROMPT)
