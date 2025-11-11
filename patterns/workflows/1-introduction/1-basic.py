import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're name is SERA and your a mechanical assistant."},
        {
            "role": "user",
            "content": "hi.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)
