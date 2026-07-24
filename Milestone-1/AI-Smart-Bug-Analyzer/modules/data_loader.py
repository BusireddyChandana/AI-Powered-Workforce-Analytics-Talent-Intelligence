import pandas as pd


def load_bug_dataset(file_path):
    """
    Load bug dataset from CSV.
    """

    df = pd.read_csv(file_path)

    print(f"Dataset Loaded Successfully!")
    print(f"Total Bug Reports: {len(df)}")

    return df


def prepare_bug_data(df):
    """
    Select useful columns for AI analysis.
    """

    selected_columns = [
        "bug_id",
        "product_name",
        "component_name",
        "short_description",
        "long_description",
        "severity_category",
        "status_category",
        "resolution_category"
    ]

    df = df[selected_columns]

    return df