# Artifact Data Cleaning Project

This repository contains two Python scripts I wrote to clean up and filter messy artifact tracking data. It shows how I approach data cleanup using both a popular library (Pandas) and standard, everyday Python.

## What This Code Does
* **Cleans up messy text:** Fixes formatting issues like accidental spaces and incorrect capitalization so the data is uniform.
* **Filters for specific regions:** Searches the data to pull out only the specific artifacts located in Washington.
* **Handles numbers:** Converts text data into actual numbers so it can filter out records below a certain threshold.
* **Skips broken data:** Uses error handling so the script doesn't crash if a line of text is broken or formatted incorrectly.

## Tools & Skills Used
* **Python** (Core file reading/writing, loops, and logic)
* **Pandas** (DataFrames and basic data manipulation)
