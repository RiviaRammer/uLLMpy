import uAI
import time

api_key = 'sk-1u112r9ruxbgb1l6ps5sj7rpo3fouxs6'
client = uAI.DeepSeek(api_key=api_key)

# Start a new conversation.
client.chat("Who r u?", mode="new")

# Continue the conversation.
client.chat("I'm a coder.", mode="continue")

message='Show me some color.'
client.chat(message, mode="continue")

# Get the chat history.
print(client.chat_history)
