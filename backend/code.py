from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
import sys
import os

def construct_index():
    documents = SimpleDirectoryReader("./documents").load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)
    index.save_to_disk('index')
    return index

def ask_lenny():
    index = GPTSimpleVectorIndex.load_from_disk('index')
    while True: 
        query = input("What do you want to ask Lenny? ")
        response = index.query(query, response_mode="compact")
        print(response)

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "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"
    construct_index()
    ask_lenny()
