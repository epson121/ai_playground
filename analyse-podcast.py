## need to have Open AI api key

# export OPENAI_API_KEY=<your_key>

import os
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader


path = "<path-to-podcast-file>"
if os.path.exists(path):
	index = GPTSimpleVectorIndex.load_from_disk(path)
else:
	documents = SimpleDirectoryReader('data').load_data()
	index = GPTSimpleVectorIndex(documents)
	index.save_to_disk(path)

response = index.query("Who are the hosts, and what is the name of the podcast?")
print(response)

response = index.query("Can you provide summary of this episode in a form of bullet points? Preferrably with timestamps.")
print(response)
