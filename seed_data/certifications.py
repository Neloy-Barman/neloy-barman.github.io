"""
Order of Insertion (certifications): title, issuer, issue_date, expiry_date,
         credential_id, credential_url, logo_url, featured, display_order,
         course_link, estimated_effort, description, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import certifications_path


def seed_certifications(conn):

    # Certifications
    certs = load_csv(
        csv_path=certifications_path,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO certifications
        (title, issuer, issue_date, expiry_date, credential_id, credential_url,
         logo_url, featured, display_order, course_link, estimated_effort, description, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        certs,
    )
    conn.commit()

    print("[SEED] certifications done.")
