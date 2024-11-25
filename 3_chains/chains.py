from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
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

# Create individual runnables (steps in the chain)
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

# Create the RunnableSequence (equivalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

# Run the chain
response = chain.invoke({"subject": "math", "math_operation": "square root", "number": 36})

# Output
print(response)
