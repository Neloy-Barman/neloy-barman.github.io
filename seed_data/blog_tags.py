"""
Order of Insertion (blog_post_tags): post_id, tag_id, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import blog_tags_path


def seed_blog_post_tags(conn):

    # Blog Post Tags
    blog_post_tags = load_csv(
        csv_path=blog_tags_path,
    )
    conn.executemany(
        """
        INSERT OR IGNORE INTO blog_post_tags (post_id, tag_id, is_visible, is_deleted)
        VALUES (?, ?, ?, ?)
    """,
        blog_post_tags,
    )
    conn.commit()

    print("[SEED] blog post tags done.")
