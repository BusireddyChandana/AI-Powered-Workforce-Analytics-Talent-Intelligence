from modules.rag_pipeline import add_bug_to_database, search_similar_bugs


bug_text = """
Application crashes during login because of null pointer exception.
Object was not initialized before accessing.
"""


add_bug_to_database(
    "BUG-001",
    bug_text
)


result = search_similar_bugs(
    "Login page crashes due to null value"
)


print(result)