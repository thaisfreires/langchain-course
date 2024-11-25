# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# Load environment variables from .env
load_dotenv()

# Create a Groq model
llm = ChatGroq(model="mixtral-8x7b-32768")

messages = [
    ("system", "You are a helpful assistant that explains what how a chat model is made. Give me an example of a chat model."),
    ("human", "How is a chat model created?"),
]

# Invoke the model with a message
ai_msg = llm.invoke(messages)

#print("Content only:" )
print(ai_msg.content)