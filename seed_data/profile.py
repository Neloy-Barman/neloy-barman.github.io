"""
Order of Insertion: full_name, title, tagline, bio_short, bio_long,
         avatar_url, resume_url, email, phone, location, available_for_work,
         is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import profile_path


def seed_profile(conn):

    # Profile
    profile_data = load_csv(
        csv_path=profile_path,
    )

    conn.execute(
        """
        INSERT OR IGNORE INTO profile
        (full_name, title, tagline, bio_short, bio_long,
         avatar_url, resume_url, email, phone, location, available_for_work, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        profile_data[0],
    )
    conn.commit()
    print("[SEED] profile done.")
