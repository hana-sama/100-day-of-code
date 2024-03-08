import openai
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

class Chatbot:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
    

    def get_response(self, user_input):
        response = openai.completions.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text

        return response

if __name__=="__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Tell me the probability of Donald Trump can win 2024 U.S. presidential election")
    print(response)