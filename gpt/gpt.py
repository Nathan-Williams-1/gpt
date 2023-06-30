"""

Chatting with ChatGPT

Issues with current quota, can't have conversations.
Might have to pay?

"""
# %% Imports
import os
import openai
from dotenv import load_dotenv
load_dotenv()

# %% Main
openai.api_key = os.getenv('GPT_API_KEY')
engine = 'text-davinci-003'
prompt = 'Is this working?'

completion = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    max_tokens=1_024,
    n=1,
    stop=None,
    temperature=0.5,
    )
response = completion.choices[0].text