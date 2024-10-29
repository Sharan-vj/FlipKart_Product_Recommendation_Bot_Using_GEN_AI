# Import Dependencies
import pandas as pd
from pathlib import Path
from langchain_core.documents import Document


# Data Path
data_path = Path('data/flipkart_reviews.csv')


# Data Converter
def data_converter():
    product_data = pd.read_csv(data_path)
    data = product_data[['product_title', 'review']]

    product_list = []
    for index, row in data.iterrows():
        object = {
            "product_name": row["product_title"],
            "review": row["review"]
        }
        product_list.append(object)

    docs = []
    for item in product_list:
        metadata = {"product_name": item["product_name"]}
        document = Document(page_content=item["review"], metadata=metadata)
        docs.append(document)
    return docs
