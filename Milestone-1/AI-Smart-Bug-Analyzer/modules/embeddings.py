from sentence_transformers import SentenceTransformer


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts):
    """
    Convert bug report text into vector embeddings.
    """

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings