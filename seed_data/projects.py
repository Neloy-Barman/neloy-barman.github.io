"""
Order of Insertion (projects): title, slug, short_desc, long_desc, image_url,
         demo_url, github_url, workflow_url, dashboard_url, integration_url ,
         status, featured, display_order, publish_date, is_visible, is_deleted
"""

from utils.csv_loader import load_csv
from seed_data.paths import projects_path
from seed_data.project_tags import seed_project_tags


def seed_projects(conn):

    # Projects
    projects = load_csv(
        csv_path=projects_path,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO projects
        (title, slug, short_desc, long_desc, image_url,
        demo_url, github_url, workflow_url, dashboard_url, integration_url,
        status, featured, display_order, publish_date, is_visible, is_deleted)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        projects,
    )
    conn.commit()

    print("[SEED] projects done.")

    seed_project_tags(
        conn=conn,
    )
