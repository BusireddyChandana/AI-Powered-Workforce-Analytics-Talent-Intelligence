from reports.executive_summary import generate_executive_summary


def create_report(df, filename="executive_workforce_report.txt"):
    """
    Create executive summary report file
    """

    report_content = generate_executive_summary(df)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(report_content)

    return filename