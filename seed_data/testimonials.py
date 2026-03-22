"""
Order of Insertion (testimonials): author_name, author_title, author_company,
         author_avatar, content, rating, relationship, featured, display_order,
         is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import testimonials_path


def seed_testimonials(conn):

    # Testimonials
    testimonials = load_csv(
        csv_path=testimonials_path,
    )
    conn.executemany(
        """
        INSERT OR IGNORE INTO testimonials
        (author_name, author_title, author_company, author_avatar, content,
         rating, relationship, featured, display_order, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        testimonials,
    )
    conn.commit()
    print("[SEED] testimonials done.")
