"""
Order of Insertion (analytics_config): analytics_enabled, provider, tracking_id, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import analytics_path


def seed_analytics(conn):

    analytics_config = load_csv(
        csv_path=analytics_path,
    )

    conn.execute(
        """
        INSERT OR IGNORE INTO analytics_config
        (analytics_enabled, provider, tracking_id, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?)
    """,
        analytics_config,
    )
    conn.commit()
    print("[SEED] analytics_config done.")
