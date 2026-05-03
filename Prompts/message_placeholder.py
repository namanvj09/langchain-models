from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
#Chat template

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []
# Load chat history

with open("Prompts/chat_history.txt") as f:
    chat_history.extend(f.readlines())

print(chat_history)


#Create Prompt

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'What is the status of my refund request?'
})

print(prompt)
