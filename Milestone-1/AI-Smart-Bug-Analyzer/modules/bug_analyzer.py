def analyze_bug(title, description, stack_trace):

    text = f"""
    Title: {title}
    Description: {description}
    Stack Trace: {stack_trace}
    """

    analysis = {
        "bug_title": title,
        "possible_issue": "Based on stack trace and description, a runtime issue may exist.",
        "severity": "High",
        "suggested_action": "Check code logic, initialization and error handling."
    }

    return text, analysis