"""
Order of Insertion (skills): category_id, name, proficiency, display_order, icon_url, is_visible, is_deleted
Note: badge_url is stored in the icon_url column
"""

from utils.csv_loader import load_csv
from seed_data.paths import skills_path
from seed_data.skill_categories import seed_skill_categries


def seed_skills(conn):

    # Seed Categories
    seed_skill_categries(conn)

    # Skills
    skills_data = load_csv(
        csv_path=skills_path,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO skills
        (category_id, name, proficiency, display_order, icon_url, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        skills_data,
    )
    conn.commit()
    print("[SEED] skills done.")
