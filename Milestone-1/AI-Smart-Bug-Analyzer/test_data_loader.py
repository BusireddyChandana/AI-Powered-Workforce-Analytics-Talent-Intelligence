from modules.data_loader import load_bug_dataset, prepare_bug_data

df = load_bug_dataset("data/mozilla_bug_report_data.csv")

df = prepare_bug_data(df)

print("\nFirst 5 Bug Reports:\n")
print(df.head())