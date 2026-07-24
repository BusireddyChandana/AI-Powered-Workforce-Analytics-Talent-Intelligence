import streamlit as st
import requests


st.set_page_config(
    page_title="AI Smart Bug Analyzer and Fix Advisor",
    page_icon="🐞"
)


st.title("🐞 AI Smart Bug Analyzer and Fix Advisor")

st.write(
    "AI-based bug analysis, similar bug retrieval and fix recommendation system"
)


# Bug inputs

title = st.text_input("Bug Title")


description = st.text_area(
    "Bug Description"
)


stack_trace = st.text_area(
    "Stack Trace / Error Log"
)


# File upload option

uploaded_file = st.file_uploader(
    "Upload Bug Report / Code / Log File",
    type=[
        "txt",
        "log",
        "py",
        "java",
        "cpp",
        "json"
    ]
)


if uploaded_file:

    file_content = uploaded_file.read().decode(
        "utf-8",
        errors="ignore"
    )

    stack_trace = file_content

    st.subheader("Uploaded File Content")

    st.text_area(
        "File Preview",
        file_content,
        height=200
    )


# Analyze button

if st.button("🔍 Analyze Bug"):


    if title and description and stack_trace:


        response = requests.post(
            "http://127.0.0.1:8000/analyze-bug",
            json={
                "title": title,
                "description": description,
                "stack_trace": stack_trace
            }
        )


        if response.status_code == 200:


            result = response.json()


            st.success(
                "Bug Analysis Completed ✅"
            )


            analysis = result.get(
                "analysis",
                {}
            )


            st.subheader(
                "🔍 Bug Analysis Result"
            )


            st.write(
                "### 🐞 Bug Title"
            )
            st.write(
                analysis.get(
                    "bug_title",
                    "N/A"
                )
            )


            st.write(
                "### ⚠️ Severity"
            )
            st.write(
                analysis.get(
                    "severity",
                    "N/A"
                )
            )


            st.write(
                "### 🔎 Possible Issue"
            )
            st.write(
                analysis.get(
                    "possible_issue",
                    "N/A"
                )
            )


            st.write(
                "### 🔧 Suggested Fix"
            )
            st.write(
                analysis.get(
                    "suggested_action",
                    "N/A"
                )
            )


            st.write(
                "### 📚 Similar Historical Bugs"
            )


            similar = result.get(
                "similar_historical_bugs",
                {}
            )


            if "ids" in similar:

                for bug in similar["ids"][0]:

                    st.write(
                        "✅",
                        bug
                    )


        else:

            st.error(
                "Backend error"
            )


    else:

        st.warning(
            "Please fill all fields or upload a file"
        )