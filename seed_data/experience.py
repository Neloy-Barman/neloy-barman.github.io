"""
Order of Insertion (experience): company, position, location, employment_type,
         start_date, end_date, is_current, description, logo_url, company_url, display_order,
         is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import experiences_path
from seed_data.achievements import seed_achievements


def seed_experience(conn):

    # Experiences
    experiences = load_csv(
        csv_path=experiences_path,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO experience
        (company, position, location, employment_type, start_date, end_date,
         is_current, description, logo_url, company_url, display_order, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        experiences,
    )
    conn.commit()

    print("[SEED] experience done.")

    # Seed Achievements
    seed_achievements(conn)
