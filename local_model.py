
from ollama import chat
from google import genai

response = chat(
    model="gemma3:1b",
    messages=[
        {
            'role': "user",
            'content': "Explain machine learning?"
        }
    ]
)

print(response.message.content)


# 01_streaming:

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain machine learning in exactly 20 short points.",
    stream=True
)

for event in stream:
    if event.event_type == "step.delta":
        if event.delta.type == "text":
            print(event.delta.text, end="", flush=True)


# 02_Prompting:

response = client.interactions.create(
    model="gemini-3.6-flash",
    input="Give me the names of 3 AI startups.",
    generation_config={
        "temperature": 1.0,
        "max_output_tokens": 10000
    }
)

print(response.output_text)
