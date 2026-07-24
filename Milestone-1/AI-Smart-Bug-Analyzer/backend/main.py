from fastapi import FastAPI
from pydantic import BaseModel

from modules.bug_analyzer import analyze_bug
from modules.rag_pipeline import search_similar_bugs


app = FastAPI(
    title="AI Smart Bug Analyzer API",
    description="AI-based bug analysis and fix recommendation system",
    version="1.0"
)


class BugReport(BaseModel):
    title: str
    description: str
    stack_trace: str


@app.get("/")
def home():
    return {
        "message": "AI Smart Bug Analyzer Backend is running!"
    }


@app.post("/analyze-bug")
def analyze_bug_report(report: BugReport):

    # AI analysis
    bug_text, analysis = analyze_bug(
        report.title,
        report.description,
        report.stack_trace
    )

    # Search similar bugs from ChromaDB
    similar_bugs = search_similar_bugs(
        bug_text
    )

    return {
        "status": "success",
        "analysis": analysis,
        "similar_historical_bugs": similar_bugs
    }