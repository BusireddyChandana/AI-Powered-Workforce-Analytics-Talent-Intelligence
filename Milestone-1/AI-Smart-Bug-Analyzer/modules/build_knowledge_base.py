import pandas as pd

from modules.rag_pipeline import add_bug_to_database


def build_knowledge_base(csv_file):
    """
    Read bug dataset and store bug reports in ChromaDB.
    """

    df = pd.read_csv(csv_file)

    print("Total bugs found:", len(df))

    for index, row in df.iterrows():

        bug_id = str(row["bug_id"])

        text = f"""
        Product: {row.get('product_name', '')}
        Component: {row.get('component_name', '')}

        Bug Description:
        {row.get('short_description', '')}

        Details:
        {row.get('long_description', '')}

        Severity:
        {row.get('severity_category', '')}

        Status:
        {row.get('status_category', '')}
        """

        add_bug_to_database(
            bug_id,
            text
        )

        if index % 100 == 0:
            print(f"{index} bugs added...")


    print("Knowledge base created successfully!")


if __name__ == "__main__":

    datasets = [
    "data/mozilla_bug_report_data.csv",
    "data/gcc_bug_report_data.csv",
    "data/gnome_bug_report_data.csv",
    "data/freedesktop_bug_report_data.csv"
    "data/freedesktop_bug_report_data.csv"
    ]


    for dataset in datasets:
        print("\nLoading:", dataset)

        build_knowledge_base(dataset)