from sentence_transformers import SentenceTransformer

# Load the same model used in generate_embeddings.py.
# You must use the same model for both document embeddings and query embeddings:
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)


def get_query_embedding(text, precision="float32"):
    # input_type="query" optimizes the vector for search retrieval.
    # Use "document" only when embedding text you plan to store in MongoDB.
    return model.encode(text, precision=precision).tolist()


user_query = "I need an automated, scalable system for serious information storage"
query_vector = get_query_embedding(user_query)
print(f"Query: '{user_query}'")
print(f"Vector dimensions: {len(query_vector)}")
print(f"First 5 values: {query_vector[:5]}")
