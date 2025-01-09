from pydantic_ai import Agent
from dotenv import load_dotenv
from pydantic_ai.models.gemini import GeminiModel
from tools import basic_search
load_dotenv()

model = GeminiModel("gemini-1.5-flash")

rag_agent = Agent(
    model,
    system_prompt="You must answer the user question using 'rag_search' tool to search for infomation "
    "and answer the user question",
    result_retries=2
)

@rag_agent.tool_plain
def rag_search(question: str) -> str:
    """
    This tool allow you to access the pdf file to answer the user question
    the higher the score the better the similarity, please be aware with it!

    Args:
        question (str): the key sentence to search the pdf file vector store,
        for example: if the user question is "What is the capital of France?",
        the key sentence is "Capital of France"
    """
    return basic_search(question)


def run_rag_agent():
    question = input("Enter your question: ")
    result = rag_agent.run_sync(question)
    print(result.data)

if __name__ == "__main__":
    run_rag_agent()


