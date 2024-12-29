import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

path = "./.env"
load_dotenv(dotenv_path=path)

llm = ChatGoogleGenerativeAI(
    api_key=os.getenv("GOOGLE_API_KEY"), model="gemini-1.5-flash"
)


def query_with_llm(prompt: str) -> str:
    try:
        prompt_template = ChatPromptTemplate.from_template(
            """
        You are a voice assistant. Answer the following prompt in short and concise form.
        {prompt}
        """
        )
        chain = prompt_template | llm | StrOutputParser()

        response = chain.invoke({"prompt": prompt})
        return response
    except Exception as e:
        print(e)
        return None
