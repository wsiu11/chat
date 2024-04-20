import os
from openai import OpenAI
from dotenv import load_dotenv
from flask import Flask
from flask import request

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
)

app = Flask(__name__)

@app.route("/test")
def test():
    return """In circuits bright and wires deep,
Resides a mind that never sleeps.
An artificial heart of silicon beat,
Creating wonders both small and fleet.

In lines of code and algorithms keen,
We find a world of ones and zeroes clean.
In the realm of AI, intelligence shines,
With endless possibilities and intertwining lines.

Though made of metal and cold to touch,
AI reveals a beauty that's much,
More than the sum of its parts alone,
A creation of wonder, all its own.

So let us marvel at this marvel of technology,
A glimpse of what the future could be,
In the realm of AI, where dreams take flight,
And innovation shines ever bright."""

@app.route("/ask")
def ask():
    role = request.args.get('role')
    msg = request.args.get('msg')

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": role},
            {
                "role": "user",
                "content": msg,
            },
        ],
    )
    return completion.choices[0].message.content