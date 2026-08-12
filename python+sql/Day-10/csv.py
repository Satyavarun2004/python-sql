import asyncio
import pandas as pd


def load_data(file_name):
    """Load CSV data."""
    return pd.read_csv(file_name)


def clean_data(data):
    """Handle missing values."""
    data["Marks"] = data["Marks"].fillna(0)
    return data


def analyze_data(data):
    """Analyze student data."""

    average_marks = data["Marks"].mean()

    high_scorers = data.loc[
        data["Marks"] >= 80,
        ["Name", "Marks"]
    ]

    print("\n----- Data Analysis -----")
    print(f"Average Marks: {average_marks:.2f}")

    print("\nStudents with marks >= 80:")
    print(high_scorers)

    return data


async def process_csv(file_name):
    """Asynchronously process CSV data."""

    print("Loading CSV file...")

    # Simulate asynchronous I/O
    await asyncio.sleep(1)

    data = load_data(file_name)

    print("CSV loaded successfully.")

    data = clean_data(data)

    print("Missing data handled.")

    data = analyze_data(data)

    data.to_excel("cleaned_students.xlsx", index=False)

    print("\nCleaned data saved to Excel.")


async def main():
    file_name = input("Enter CSV file name: ")

    try:
        await process_csv(file_name)

    except FileNotFoundError:
        print("Error: CSV file not found.")


asyncio.run(main())


