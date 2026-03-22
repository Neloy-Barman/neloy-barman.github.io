"""
Order of Insertion (project_tags): project_id, tag_id, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import project_tags_path


def seed_project_tags(conn):

    # Project Tags
    project_tags = load_csv(
        csv_path=project_tags_path,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO project_tags (project_id, tag_id,is_visible, is_deleted)
        VALUES (?, ?, ?, ?)
    """,
        project_tags,
    )
    conn.commit()

    print("[SEED] project tags done.")
