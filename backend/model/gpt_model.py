from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
import sys
import os

os.environ["OPENAI_API_KEY"] = "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"

def construct_index():
    global index
    if os.path.exists('index'):
      index = GPTSimpleVectorIndex.load_from_disk('index')
    else:
        documents = SimpleDirectoryReader("./documents").load_data()
        index = GPTSimpleVectorIndex.from_documents(documents)
        index.save_to_disk('index')


def ask_the_model(query):
    construct_index()
    index = GPTSimpleVectorIndex.load_from_disk('index')
    response = index.query(query, response_mode="compact")
    gpt_reply = {"reply": response.response}
    print(response)
    return gpt_reply