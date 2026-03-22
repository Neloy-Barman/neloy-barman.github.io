import csv
from pathlib import Path


def load_csv(csv_path):
    """
    Reads a CSV file and returns a list of tuples.
    Each row becomes a tuple ready for conn.executemany()
    """
    csv_path = Path(csv_path)

    if not csv_path.exists():
        print(f"[CSV ERROR] File not found: {csv_path}")
        return []

    records = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            records.append(
                tuple(None if cell.strip() == "" else cell.strip() for cell in row)
            )

    print(f"[CSV] Loaded {len(records)} records from {csv_path.name}")
    return records
