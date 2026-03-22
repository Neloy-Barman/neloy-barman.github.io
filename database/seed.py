# database/seed.py
"""
Seed script: Populates portfolio.db with placeholder data.
Run: python database/seed.py
"""

import os
import shutil
import sqlite3
from datetime import datetime

# Seed Data
from seed_data.tags import seed_tags
from seed_data.skills import seed_skills
from seed_data.profile import seed_profile
from seed_data.blogs import seed_blog_posts
from seed_data.projects import seed_projects
from seed_data.analytics import seed_analytics
from seed_data.education import seed_education
from seed_data.experience import seed_experience
from seed_data.site_config import seed_site_config
from seed_data.social_links import seed_social_links
from seed_data.testimonials import seed_testimonials
from seed_data.certifications import seed_certifications

DB_PATH = os.path.join(os.path.dirname(__file__), "portfolio.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def backup_db():
    """Backup existing DB before migration."""
    if os.path.exists(DB_PATH):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = DB_PATH.replace(".db", f"_backup_{ts}.db")
        shutil.copy2(DB_PATH, backup_path)
        print(f"[BACKUP] Database backed up to: {backup_path}")


def apply_schema(conn):
    with open(SCHEMA_PATH, "r") as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    conn.commit()
    print("[SCHEMA] Applied successfully.")


def main():
    print("=" * 60)
    print("Portfolio Database Seed Script")
    print("=" * 60)

    backup_db()
    conn = get_connection()

    try:
        apply_schema(conn)
        seed_site_config(conn)
        seed_social_links(conn)
        seed_profile(conn)
        seed_education(conn)
        seed_experience(conn)
        seed_skills(conn)
        seed_tags(conn)
        seed_projects(conn)
        seed_certifications(conn)
        seed_blog_posts(conn)
        seed_testimonials(conn)
        # seed_analytics(conn)
        print("=" * 60)
        print("[SUCCESS] Database seeded successfully.")
        print("=" * 60)
    except Exception as e:
        conn.rollback()
        print(f"[ERROR] Seeding failed: {e}")
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
