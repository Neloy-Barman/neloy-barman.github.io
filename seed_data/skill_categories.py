"""
Order of Insertion (skill_categories): name, icon_class, display_order, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import skill_categories_path


"""
Instead of the direct variable, I want it to read data from my given CSV path and then 
"""


def seed_skill_categries(conn):
    # Categories
    categories = load_csv(
        csv_path=skill_categories_path,
    )
    conn.executemany(
        """
        INSERT OR IGNORE INTO skill_categories (name, icon_class, display_order, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?)
    """,
        categories,
    )
    conn.commit()
    print("[SEED] skill categories done.")
