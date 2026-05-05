from pymongo.mongo_client import MongoClient
from pymongo.operations import SearchIndexModel
import time

# Replace the placeholder with your Atlas connection string:
mongodb_client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-vectorsearch"
)

# Point to the same database and collection you used in the previous step:
database = mongodb_client["sample_db"]
collection = database["documents"]

# Define the vector search index.
# The three required fields tell MongoDB what to index and how to compare vectors:
search_index_model = SearchIndexModel(
    definition={
        "fields": [
            {
                "type": "vector",
                "path": "embedding",      # The field name from generate_embeddings.py
                "numDimensions": 768,     # nomic-embed-text-v1 always outputs 768 dimensions
                "similarity": "cosine"    # Recommended similarity function for this model
            }
        ]
    },
    name="vector_index",
    type="vectorSearch"
)

result = collection.create_search_index(model=search_index_model)
print("New search index named " + result + " is building.")

# Poll every five seconds until the index is ready to accept queries:
print("Polling to check if the index is ready. This may take up to a minute.")

predicate = lambda index: index.get("queryable") is True

while True:
    indices = list(collection.list_search_indexes(result))
    if len(indices) and predicate(indices[0]):
        break
    time.sleep(5)

print(result + " is ready for querying.")

mongodb_client.close()
