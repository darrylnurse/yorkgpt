import os
from dotenv import load_dotenv
from openai import OpenAI

# load the dotenv module so we can get that key from the .env file
load_dotenv()

# we can get that key from the .env file
openai_key = os.getenv('OPENAI_KEY')

# this function will be called in the server module
def get_model_response(prompt):
    
    # initialize new OpenAI instance
    client = OpenAI(
        api_key=openai_key
    )

    # generate the chat completions based on the prompt parameter
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )
   
    # return structure based on the ChatCompletionMessage class
    # https://github.com/openai/openai-python/blob/main/src/openai/types/chat/chat_completion_message.py
    return completion.choices[0].message.content