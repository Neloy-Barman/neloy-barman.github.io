"""
Order of Insertion: institution, degree, field_of_study, start_date, end_date, gpa,
         description, logo_url, location, display_order, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import education_path


def seed_education(conn):

    # Education
    education = load_csv(
        csv_path=education_path,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO education
        (institution, degree, field_of_study, start_date, end_date, gpa,
         description, logo_url, location, display_order, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        education,
    )
    conn.commit()
    print("[SEED] education done.")
