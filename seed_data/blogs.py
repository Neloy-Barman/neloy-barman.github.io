"""
Order of Insertion (blog_posts): title, slug, excerpt, content,
         cover_image_url, read_time, featured, publish_date,
         post_url, display_order, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import blogs_path
from seed_data.blog_tags import seed_blog_post_tags


def seed_blog_posts(conn):

    # Blog Posts
    posts = load_csv(
        csv_path=blogs_path,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO blog_posts
        (title, slug, excerpt, content, cover_image_url, read_time, featured, publish_date, post_url, display_order, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        posts,
    )
    conn.commit()

    print("[SEED] blog_posts done.")

    seed_blog_post_tags(
        conn=conn,
    )
