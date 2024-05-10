from typing import List
from promptflow import tool
# from promptflow_vectordb.core.contracts import SearchResultEntity


@tool
def generate_prompt_context(search_result: List) -> str:
    def format_doc(doc: dict):
        return f"Context: \nQuestion: {doc['Question']}\nAnswer: {doc['Answer']}"

    retrieved_docs = []
    for item in search_result:
        question = item['question']
        answer = item['answer']

        retrieved_docs.append({
            "Question": question,
            "Answer": answer
        })
    doc_string = "\n\n".join([format_doc(doc) for doc in retrieved_docs])

    return doc_string
