from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='qwen2.5', messages=[
  {
    'role': 'aiAgent',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)