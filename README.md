

# LangChain Course 

This project has a set of code examples of basic concepts of AI using the LangChain framework. I followed a course from YouTube, and the code examples provided by the instructor were combined with my own modifications and improvements. These examples aim to showcase various aspects of the LangChain framework, demonstrating its capabilities in building AI-driven applications. 

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Package Dependencies

- Langchain OpenAI
- Python Dotenv
- Langchain Groq
- Langchain Core
- Langchain Google GenAI
- Langchain Anthropic
- Langchain Google Firestore
- Langchain Community
- ChromaDB
- Tiktoken
- Langchain Chroma
- Langchain HuggingFace
- BeautifulSoup (bs4)
- Firecrawl
- Wikipedia
- Tavily Python


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file with your API keys.

OPENAI_API_KEY='YOUR_API_KEY'
ANTHROPIC_API_KEY='YOUR_API_KEY'
GOOGLE_API_KEY='YOUR_API_KEY'
GROQ_API_KEY='YOUR_API_KEY'


## Installation

1. Clone the repository

```bash
 git clone https://github.com/thaisfreires/langchain-course 

```
2. Create the virtual environment variables
```bash
py -m venv .venv
```
3. Activate the virtual environment
```bash
.venv\Scripts\activate
```
4. Run the file requirements.txt to dependency tools
```bash
pip install -r requirements.txt
```
5. Run the code like the example:
```bash
cd 1_chat_models
 python chat_model_alternatives.py
```

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
