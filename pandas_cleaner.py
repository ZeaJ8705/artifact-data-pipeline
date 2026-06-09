import pandas as pd

# Load the raw artifact dataset
df = pd.read_csv("artifacts.csv")

# Standardize text formatting by removing whitespace and capitalizing titles
df["Category"] = df["Category"].str.strip().str.title()

# Filter for specific regional lithic artifacts
washington_lithics = df[(df["Category"] == "Lithic") & (df["Location"] == "Washington")].copy()

# Export results with custom tracking row numbers
washington_lithics.to_csv("filtered_output.csv", index=True, index_label="Row_Number")

print("CSV spreadsheet filtered with custom row numbers!")
