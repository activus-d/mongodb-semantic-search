from sentence_transformers import SentenceTransformer
from pymongo import MongoClient

# Load the free, open-source embedding model.
# The model downloads from Hugging Face on first run and saves locally:
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)


def get_embedding(text, precision="float32"):
    # input_type="document" optimizes the vector for storage and retrieval.
    # Use this when embedding text you plan to store in MongoDB:
    return model.encode(text, precision=precision).tolist()


# Replace the placeholder with your Atlas connection string:
mongodb_client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-semantic-search"
)

collection = mongodb_client["sample_db"]["documents"]

# Sample data:
sample_documents = [
    {
        "title": "MongoDB Atlas",
        "text": "MongoDB Atlas is a fully managed cloud database."
    },
    {
        "title": "Vector Search",
        "text": "Vector search finds results based on semantic meaning."
    },
    {
        "title": "Nomic AI",
        "text": "nomic-embed-text-v1 is a free, open-source embedding model."
    },
]

docs_to_insert = []

for doc in sample_documents:
    embedding = get_embedding(doc["text"])
    docs_to_insert.append({
        "title": doc["title"],
        "text": doc["text"],
        # The vector lives alongside your original data in the same document:
        "embedding": embedding
    })
# Drop the collection before each run to avoid inserting duplicate documents:
collection.drop()

result = collection.insert_many(docs_to_insert)
print(f"Inserted {len(result.inserted_ids)} documents with embeddings.")

mongodb_client.close()
