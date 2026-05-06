from generate_query_vector import get_query_embedding
from pymongo import MongoClient

# Replace the placeholder with your Atlas connection string:
mongodb_client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-vector-search"
)

collection = mongodb_client["sample_db"]["documents"]

# Generate a query vector from the user's search input:
user_query = "I need an automated, scalable system for serious information storage"
query_vector = get_query_embedding(user_query)

# Define the $vectorSearch aggregation pipeline:
pipeline = [
    {
        "$vectorSearch": {
            "index": "vector_index",      # The index created in create_vector_index.py
            "path": "embedding",          # The field that holds your stored vectors
            "queryVector": query_vector,  # The vector generated from the user's query
            "numCandidates": 150,         # How many neighbors MongoDB considers
            "limit": 10                   # How many results to return
        }
    },
    {
        "$project": {
            "_id": 0,
            "title": 1,
            "text": 1,
            "score": {
                "$meta": "vectorSearchScore"  # Relevance score for each result
            }
        }
    }
]

results = collection.aggregate(pipeline)

print(f"\nTop results for query: '{user_query}'\n")

for doc in results:
    print(f"Title: {doc['title']}")
    print(f"Text:  {doc['text']}")
    print(f"Score: {doc['score']:.4f}")
    print()

mongodb_client.close()
