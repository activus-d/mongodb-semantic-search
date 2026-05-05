# MongoDB semantic search — Python examples

This repository contains the code samples for the "How to Implement Semantic Search in MongoDB" tutorial. It covers four steps to implement semantic search:

- generating and storing vector embeddings
- creating a MongoDB Vector Search index
- converting a search query into a vector
- running a `$vectorSearch` aggregation pipeline

The steps are implemented in Python using the free `nomic-embed-text-v1` embedding model and a MongoDB Atlas free tier cluster.

## Clone the Repository

Run the following command to clone the repository to your machine:

```bash
git clone https://github.com/activus-d/mongodb-semantic-search.git
```

## Set Up Your Environment

Navigate into the project folder:

```bash
cd mongodb-semantic-search
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows, activate the virtual environment with:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install pymongo sentence-transformers einops
```

## Run the Files

Before you run any file, replace the `<USERNAME>`, `<PASSWORD>`, and `<HOST>` placeholders in the connection string with your Atlas credentials and cluster hostname.

Run the files in the following order. Each file depends on the output of the previous one.

Generate and store vector embeddings:

```bash
python generate_embeddings.py
```

Create the vector search index and wait for it to become ready:

```bash
python create_vector_index.py
```

Verify that the embedding model produces the expected output:

```bash
python generate_query_vector.py
```

Run the semantic search query and view the results:

```bash
python run_vector_search.py
```

Refer to the tutorial for a full explanation of what each script does and how the search results differ from a regular text search.
