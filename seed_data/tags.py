"""
Order of Insertion (tags): tag_id, name, slug, display_order, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import tags_path


def seed_tags(conn):
    # Tags Data
    tags = load_csv(
        csv_path=tags_path,
    )
    conn.executemany(
        """
        INSERT OR IGNORE INTO tags (tag_id, name, slug, display_order, is_visible, is_deleted) 
        VALUES (?, ?, ?, ?, ?, ?)
    """,
        tags,
    )
    conn.commit()
    print("[SEED] tags done.")
