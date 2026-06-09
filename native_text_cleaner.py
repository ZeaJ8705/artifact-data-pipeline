# Process raw text records using native Python (no external libraries)
with open("raw_artifacts.txt", "r", encoding="utf-8") as input_file:
    raw_lines = input_file.read().splitlines()

final_results = []

for item in raw_lines:
    # Case-insensitive filtering for lithic artifacts
    if "lithic" not in item.lower():
        continue
    
    # Clean whitespace and standardize casing
    cleaned_item = item.strip().title()
    
    # Parse record components and filter by numeric values
    try:
        text_part, number_part = cleaned_item.split("-")
        if int(number_part) < 3:
            continue
        final_results.append(cleaned_item)
    except ValueError:
        # Skips lines that do not match the expected 'Text-Number' format
        continue

# Save the finalized, structured text output
with open("clean_text_output.txt", "w", encoding="utf-8") as output_file:
    for artifact in final_results:
        output_file.write(artifact + "\n")

print("Text file processed successfully!")
