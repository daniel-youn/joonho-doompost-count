import datetime
import re

def determine_current_half():
    """
    Determines the current year and half (Q1/Q2) based on the current date.
    Returns a string in the format 'YYYY QX'.
    """
    current_date = datetime.datetime.now()
    year = current_date.year
    month = current_date.month

    # Determine the half: Q1 (Jan-Jun) or Q2 (Jul-Dec)
    if 1 <= month <= 6:
        half = 'Q1'
    else:
        half = 'Q2'

    return f"{year} {half}"

def load_counters(file_path):
    """
    Reads the counters from the file and returns them as a dictionary.
    """
    counters = {}
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\d{4} Q[12]) - (\d+)', line.strip())
            if match:
                key, value = match.groups()
                counters[key] = int(value)
    return counters

def save_counters(file_path, counters):
    """
    Writes the updated counters back to the file.
    """
    with open(file_path, 'w') as file:
        for key, value in sorted(counters.items()):
            file.write(f"{key} - {value}\n")

def increment_doompost_counter(file_path):
    """
    Increments the doompost counter for the current half year.
    """
    current_half = determine_current_half()
    try:
        counters = load_counters(file_path)
    except FileNotFoundError:
        counters = {}

    # Increment the counter for the current half
    if current_half in counters:
        counters[current_half] += 1
    else:
        counters[current_half] = 1

    save_counters(file_path, counters)
    print(f"Doompost recorded for {current_half}. New count: {counters[current_half]}")

if __name__ == "__main__":
    file_path = 'count.txt'
    increment_doompost_counter(file_path)
