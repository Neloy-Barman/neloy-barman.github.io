"""
Order of Insertion: key, value, description, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import site_config_path


def seed_site_config(conn):

    # Site configs
    configs = load_csv(
        csv_path=site_config_path,
    )

    conn.executemany(
        """
        INSERT OR REPLACE INTO site_config (key, value, description, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?)
    """,
        configs,
    )
    conn.commit()
    print("[SEED] site_config done.")
