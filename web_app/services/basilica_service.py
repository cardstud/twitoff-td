import basilica
import os
from dotenv import load_dotenv

API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(API_KEY)
print(type(connection))


# breakpoint()

embedding = connection.embed_sentence("hey this is a cool tweet", model='twitter')
print(embedding)
# > a list of 768 numbers

# tweets = [ "Hello world", "artificial intelligence", "another tweet here #cool"]
# embeddings = connection.embed_sentences(tweets, model="twitter")
# for embed in embeddings:
#     print("-----")
#     print(len(embed))