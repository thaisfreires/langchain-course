from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq


# Setup environment variables and messages
load_dotenv()

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 10 times 5?"),
]

print("\n---- Groc Chat Model Example ----") 

# Create a Groq model
llm = ChatGroq(model="mixtral-8x7b-32768")


ai_msg = llm.invoke(messages)
print(f"\nAnswer from AI: {ai_msg.content}")

print("\n---- Anthropic Chat Model Example ----")

# Create a Anthropic model
# Anthropic models: https://docs.anthropic.com/en/docs/models-overview

llm = ChatAnthropic(model_name="claude-3-sonnet-20240229") # type: ignore

ai_msg = llm.invoke(messages)
print(f"Answer from Anthropic: {ai_msg.content}")


print("\n---- Google Chat Model Example ----")

# https://console.cloud.google.com/gen-app-builder/engines
# https://ai.google.dev/gemini-api/docs/models/gemini

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

ai_msg = llm.invoke(messages)
print(f"\nAnswer from Google: {ai_msg.content}")