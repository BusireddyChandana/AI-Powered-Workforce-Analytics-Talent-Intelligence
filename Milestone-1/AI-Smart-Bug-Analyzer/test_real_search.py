from modules.rag_pipeline import search_similar_bugs


query = """
Application crashes when user clicks login.
Null pointer exception occurs.
"""


result = search_similar_bugs(query, results=5)

print(result)