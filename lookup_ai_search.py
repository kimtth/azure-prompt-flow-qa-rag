import os
from typing import List
from promptflow import tool
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.models import VectorizedQuery

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

@tool
def ai_vector_search(embedding, config):
    service_endpoint = config["AZURE_SEARCH_SERVICE_ENDPOINT"]
    index_name = config["AZURE_SEARCH_INDEX_NAME"]
    key = config["AZURE_SEARCH_API_KEY"]

    search_client = SearchClient(service_endpoint, index_name, AzureKeyCredential(key))
    vector_query = VectorizedQuery(vector=embedding, k_nearest_neighbors=3, fields="questionVector")

    results = search_client.search(
        vector_queries=[vector_query],
        select=["question", "answer"],
    )
    return list(results)