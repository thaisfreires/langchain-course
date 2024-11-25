from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Create a Groq model
model = ChatGroq(model="mixtral-8x7b-32768") # type: ignore

# Define prompt templates
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpfull assistant that solves {subject} problems."),
        ("human", "What is the {math_operation} of {number}?"),
    ]
)

# Define additional processing steps using RunnableLambda
uppercase_output = RunnableLambda(lambda x: x.upper())
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")

# Create the combined chain using LangChain Expression Language (LCEL)
chain = prompt_template | model | StrOutputParser() | uppercase_output | count_words

# Run the chain
result = chain.invoke({"subject": "math", "math_operation": "square root", "number": 36})

# Output
print(result)
