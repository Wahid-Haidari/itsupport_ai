from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
import sys
import os

def construct_index():
    documents = SimpleDirectoryReader("./articles").load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    index.save_to_disk('index')
    return index

def ask_helpdesk_ai():
    index = GPTSimpleVectorIndex.load_from_disk('index')
    while True:
        query = input("What do you want to ask helpdesk AI? ")
        response = index.query(query, response_mode="compact")
        print(response)

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "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"
    #construct_index()
    ask_helpdesk_ai()