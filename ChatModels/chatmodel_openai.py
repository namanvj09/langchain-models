from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-4", temperature=1.5, max_completion_tokens=120)
response = chat.invoke("Write a 5 line poem on cricket.")

print(response.content)