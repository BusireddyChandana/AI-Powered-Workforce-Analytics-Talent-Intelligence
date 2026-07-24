import chromadb
from modules.embeddings import generate_embeddings


# Create ChromaDB client
client = chromadb.PersistentClient(
    path="storage/chromadb"
)


# Create collection
collection = client.get_or_create_collection(
    name="bug_reports"
)


def add_bug_to_database(bug_id, text):
    """
    Store bug report with embedding.
    """

    embedding = generate_embeddings([text])[0]

    collection.add(
        ids=[bug_id],
        documents=[text],
        embeddings=[embedding.tolist()]
    )

    return "Bug added successfully"


def search_similar_bugs(query, results=3):
    """
    Find similar historical bugs.
    """

    query_embedding = generate_embeddings([query])[0]

    result = collection.query(
        query_embeddings=[
            query_embedding.tolist()
        ],
        n_results=results
    )

    return result