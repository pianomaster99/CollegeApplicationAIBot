import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_essay(essay_text):
    response = client.chat.completions.create(
        model="gpt-4o",   # the model to use
        messages=[
            {"role": "system", "content": "You are an essay feedback assistant. Limit yourself to 100 words"},
            {"role": "user", "content": f"Please give feedback on this essay:\n\n{essay_text}"}
        ],
        temperature = 0.5,
        max_completion_tokens = 150
    )
    return response.choices[0].message.content.strip()
