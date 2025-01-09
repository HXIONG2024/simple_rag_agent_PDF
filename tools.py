#import
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

"""
#load pdf
loader = PyPDFLoader(r"rag_file\Your PDF file path")
documents = loader.load()

#split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
)
texts = text_splitter.split_documents(documents)

#create embeddings
embeddings = OpenAIEmbeddings()

#create vector store
vectorstore = FAISS.from_documents(texts, embeddings)

#save vector store
vectorstore.save_local("rag_file/vectorstore")
"""

def basic_search(my_query: str) -> str:
    """
    search the vector store and return the result

    Args:
        my_query (str): the query word to search the vector store
    """
    #embeddings model
    embeddings = OpenAIEmbeddings()
    #load vector store
    vectorstore = FAISS.load_local(
        "rag_file/vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )
    #basic search
    docs = vectorstore.similarity_search_with_score(my_query)
    result = ""
    for info, score in docs:
        result += f"Score: {score:.4f}\nPage Content:\n{info.page_content}\n\n"
    return result

if __name__ == "__main__":
    print(basic_search("Your question"))

