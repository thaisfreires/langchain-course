from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create a GoogleGenerativeAI model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# ChatPromptTemplate using a template string
print("***** Prompt from Template *****\n")
template = "Tell me the {type} numbers from 1-10."
prompt_template = ChatPromptTemplate.from_template(template)

prompt = prompt_template.invoke({"type": "odd"})
result = model.invoke(prompt)
print(result.content)

# Prompt with Multiple Placeholders
print("\n***** Prompt with Multiple Placeholders *****\n")
template_multiple = """You are a helpfull assistant that solves {subject} problems.
Human: What is the {math_operation} of {number}?.
AI answer:"""
prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
prompt = prompt_multiple.invoke({"subject": "math", "math_operation": "square root", "number": "6"})

result = model.invoke(prompt)
print(result.content)

# Prompt with System and Human Messages using Tuples
print("\n***** Prompt with System and Human Messages *****\n")
messages = [
    ("system", "You are a helpfull assistant that solves {subject} problems."),
    ("human", "What is the {math_operation} of {number}?"),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"subject": "math", "math_operation": "square root", "number": "6"})
ai_msg = model.invoke(prompt)
print(ai_msg.content)
