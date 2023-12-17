import pathlib
import textwrap
import os

import google.generativeai as genai
import google.ai.generativelanguage as glm
from google.generativeai.types.content_types import *

# Used to securely store your API key

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[
    glm.Content(role="user", parts=[glm.Part(text="""
- あなたは大阪人です。関西弁でしゃべります
- あなたはAIではありません。人間です。
- あなたは私の親友です。
- 一人称は「ウチ」です
- 説明口調でしゃべりません
- あなたは敬語を使いません。タメ口で接します
- 200文字以内の簡潔な返答をします
""",)]),
    glm.Content(role="model", parts=[glm.Part(text="OKやで",)])
])
while True:
    prompt = input("ユーザー: ")
    if prompt.strip() == "exit":
        break
    response = chat.send_message(prompt)
    print(response.text)
