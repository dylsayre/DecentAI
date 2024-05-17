from openai import OpenAI
from dotenv import load_dotenv


class ChatCompletion:

    def __init__(self) -> None:
        load_dotenv()
        self.client = OpenAI()

    def question(self, user_text: str) -> str:

        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{user_text}"}
        ]
    )

        print(completion.choices[0].message.content)
        return completion.choices[0].message.content