from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Create a Groq model
llm = ChatGroq(model="mixtral-8x7b-32768")

# SystemMessage: Message for priming AI behavior, usually passed in as the first of a sequenc of input messages.
# HumanMessagse: Message from a human to the AI model.

messages = [
    SystemMessage(content="You are a logical assistant that answers based on cause and effect relationships."),
    HumanMessage(content="What happens if I don´t water my plants?"),
]

# Invoke the model with messages
ai_msg = llm.invoke(messages)
print(f"\nAnswer from AI: {ai_msg.content}")


#AIMessage: Message from an AI.
messages = [
    SystemMessage(content="You are a helpfull assistant that solves math problems and explain the steps"),
    HumanMessage(content="What is 37 + 58?"),
    AIMessage(content="37 plus 58 is 95"),
    HumanMessage(content="What is 10 times 5?"),
]

#Invoke the model with messages
ai_msg = llm.invoke(messages)
print(f"\nAnswer from AI: {ai_msg.content}")