from modules.embeddings import generate_embeddings

bug_text = [
    "Application crashes when user clicks login because of null pointer exception"
]

vectors = generate_embeddings(bug_text)

print("Embedding generated successfully!")
print("Vector size:", len(vectors[0]))