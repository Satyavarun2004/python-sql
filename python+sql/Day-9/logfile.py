import re
from functools import reduce


def read_log_file(file_name):
    """Read log file and return lines."""
    with open(file_name, "r") as file:
        return file.readlines()


def analyze_logs(lines):
    """Extract ERROR and WARNING messages."""

    pattern = r"^(ERROR|WARNING):.*"

    messages = list(
        filter(
            lambda line: re.search(pattern, line),
            lines
        )
    )

    messages = list(
        map(lambda line: line.strip(), messages)
    )

    return messages


def count_messages(messages):
    """Count total error and warning messages."""

    total = reduce(
        lambda count, _: count + 1,
        messages,
        0
    )

    return total


file_name = input("Enter log file name: ")

try:
    lines = read_log_file(file_name)

    messages = analyze_logs(lines)

    print("\n----- Errors and Warnings -----")

    for message in messages:
        print(message)

    total = count_messages(messages)

    print("\nTotal Errors/Warnings:", total)

except FileNotFoundError:
    print("Error: Log file not found.")