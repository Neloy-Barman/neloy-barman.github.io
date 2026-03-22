"""
Order of Insertion (experience_achievements): experience_id, achievement, display_order, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import achievements_path


def seed_achievements(conn):

    # Achievements
    achievements_data = load_csv(
        csv_path=achievements_path,
    )
    conn.executemany(
        """
        INSERT OR IGNORE INTO experience_achievements
        (experience_id, achievement, display_order, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?)
    """,
        achievements_data,
    )
    conn.commit()
    print("[SEED] achievements done.")
