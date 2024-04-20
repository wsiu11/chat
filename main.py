import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
)

help = input("What kind of assistance do you need today?\n")

while True:
    msg = input("Please enter your question.\n")
    if msg == "":
        quit()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a assistant for "+help},
            {
                "role": "user",
                "content": msg,
            },
        ],
    )
    print(completion.choices[0].message.content)
