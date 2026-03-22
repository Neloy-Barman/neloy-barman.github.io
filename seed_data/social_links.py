"""
Order of Insertion: platform, url, icon_class, display_order, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import social_links_path


def seed_social_links(conn):

    # Social Links Path
    social_links = load_csv(
        csv_path=social_links_path,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO social_links (platform, url, icon_class, display_order, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        social_links,
    )
    conn.commit()
    print("[SEED] social_links done.")
