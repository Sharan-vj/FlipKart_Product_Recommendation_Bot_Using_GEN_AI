# Import Dependencies
import os
from dotenv import load_dotenv
from langchain_astradb import AstraDBVectorStore
from langchain_openai.embeddings import OpenAIEmbeddings
from flipkart_ecom.data_converter import data_converter


# Load all environment variables from .env file
load_dotenv()

# Store all variables
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")


embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=OPENAI_API_KEY
)


def data_ingestion(status):
    vstore = AstraDBVectorStore(
        embedding=embeddings,
        collection_name='flipkart',
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
        namespace=ASTRA_DB_KEYSPACE
    )

    storage = status
    if storage == None:
        docs = data_converter()
        insert_ids = vstore.add_documents(docs)
    else:
        return vstore
    return vstore, insert_ids


if __name__ == '__main__':
    vstore, insert_ids = data_ingestion(None)
    print(f"\n Inserted {len(insert_ids)} documents.")
    results = vstore.similarity_search(query="Can you tell me the low budget headphone")
    for res in results:
        print(f"\n {res.page_content} [{res.metadata}]")
        